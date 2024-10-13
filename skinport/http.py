"""
MIT License

Copyright (c) 2022 PaxxPatriot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import asyncio
import json
import logging
import ssl
import sys
from typing import Any, Dict, Iterable, List, Optional, Union

import aiohttp

from skinport import __version__

from .errors import (
    AuthenticationError,
    HTTPException,
    InsufficientFunds,
    InternalServerError,
    InvalidScope,
    NotFound,
)

_log = logging.getLogger(__name__)


async def json_or_text(response: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]:
    text = await response.text(encoding="utf-8")
    try:
        if "application/json" in response.headers["content-type"]:
            return json.loads(text)
    except KeyError:
        pass

    return text


class Route:
    BASE = "https://api.skinport.com/v1"

    def __init__(self, method: str, path: str) -> None:
        self.path: str = path
        self.method: str = method
        self.url: str = self.BASE + self.path


class HTTPClient:
    def __init__(
        self,
        *,
        proxy: Optional[str] = None,
        proxy_auth: Optional[aiohttp.BasicAuth] = None,
    ) -> None:
        # Checks if the skinport.Client was initialized before or after the event loop started
        # If it was not initialized, you have to call start_session()
        try:
            asyncio.get_running_loop()
            self.__session = aiohttp.ClientSession()
        except RuntimeError:
            self.__session = None
        self.auth = None
        self.proxy: Optional[str] = proxy
        self.proxy_auth: Optional[aiohttp.BasicAuth] = proxy_auth
        self.ratelimit_lock: asyncio.Lock = asyncio.Lock()

        user_agent = "skinport.py {0}) Python/{1[0]}.{1[1]} aiohttp/{2}"
        self.user_agent: str = user_agent.format(__version__, sys.version_info, str(aiohttp.__version__))  #

    def set_auth(self, client_id: str, client_secret: str) -> None:
        self.auth = aiohttp.BasicAuth(login=client_id, password=client_secret)

    async def close(self) -> None:
        if self.__session:
            await self.__session.close()

    async def start_session(self):
        self.__session = aiohttp.ClientSession()

    async def request(
        self,
        route: Route,
        params: Optional[Iterable[Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> Any:
        method = route.method
        url = route.url

        # header creation
        headers: Dict[str, str] = {
            "User-Agent": self.user_agent,
        }

        kwargs["headers"] = headers

        if params:
            kwargs["params"] = params

        # Pinning to TLS v1.3 (thanks CloudFlare)
        ssl_context = ssl.create_default_context()
        ssl_context.minimum_version = ssl.TLSVersion.TLSv1_3
        ssl_context.maximum_version = ssl.TLSVersion.TLSv1_3

        async with self.ratelimit_lock:
            for _ in range(2):
                async with self.__session.request(method, url, auth=self.auth, ssl=ssl_context, **kwargs) as response:
                    _log.debug(f"{method} {url} with {kwargs} has returned {response.status}")

                    data = await json_or_text(response)

                    if 300 > response.status >= 200:
                        _log.debug(f"{method} {url} has received {data}")
                        return data

                    if response.status in {500, 503}:
                        raise InternalServerError(response, data)

                    if response.status == 401:
                        raise AuthenticationError(response, data)
                    if response.status == 402:
                        raise InsufficientFunds(response, data)
                    if response.status == 403:
                        raise InvalidScope(response, data)
                    if response.status == 404:
                        raise NotFound(response, data)
                    if response.status == 429:
                        # We are getting rate-limited, read retry-after header and try again
                        retry_after = int(headers.get("Retry-After", 60))
                        _log.debug(f"{method} {url} is getting rate-limited, retry after {retry_after} seconds")
                        await asyncio.sleep(retry_after)
                        continue
                    raise HTTPException(response, data)

    async def get_items(self, **parameters: Any) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", "/items"), **parameters)

    async def get_sales_history(self, **parameters: Any) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", "/sales/history"), **parameters)

    async def get_sales_out_of_stock(self, **parameters: Any) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", "/sales/out-of-stock"), **parameters)

    async def get_account_transactions(self, **parameters: Any) -> Dict[str, Any]:
        return await self.request(Route("GET", "/account/transactions"), **parameters)
