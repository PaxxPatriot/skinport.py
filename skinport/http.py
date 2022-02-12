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

import base64
import logging
import sys
from typing import (
    Any,
    Dict,
    Iterable,
    Optional,
)
from urllib.parse import quote as _uriquote

import aiohttp

from . import __version__
from .errors import (
    AuthenticationError,
    Forbidden,
    InsufficientFunds,
    NotFound,
    InternalServerError,
)

_log = logging.getLogger(__name__)


class Route:
    BASE = "https://api.skinport.com/v1"

    def __init__(self, method: str, path: str) -> None:
        self.path: str = path
        self.method: str = method
        self.url: str = self.BASE + self.path


class HTTPClient:
    def __init__(self) -> None:
        self.token = None
        self.__session = None

        user_agent = "skinport.py {0}) Python/{1[0]}.{1[1]} aiohttp/{2}"
        self.user_agent: str = user_agent.format(
            __version__, sys.version_info, aiohttp.__version__
        )

    async def set_token(self, client_id: str, client_secret: str) -> Optional[str]:
        self.__session = aiohttp.ClientSession()
        if client_id and client_secret:
            self.token = base64.b64encode(
                f"{client_id}:{client_secret}".encode()
            ).decode()
        return None

    async def close(self) -> None:
        if self.__session:
            await self.__session.close()

    async def request(
        self,
        route: Route,
        params: Optional[Iterable[Dict[str, Any]]] = None,
        **kwargs: Any,
    ):
        method = route.method
        url = route.url

        # header creation
        headers: Dict[str, str] = {
            "User-Agent": self.user_agent,
        }

        if self.token is not None:
            headers["Authorization"] = f"Basic {self.token}"

        kwargs["headers"] = headers

        if params:
            kwargs["params"] = params

        async with self.__session.request(method, url, **kwargs) as response:
            _log.debug(f"{method} {url} with {kwargs} has returned {response.status}")

            data = await response.json()

            if 300 > response.status >= 200:
                _log.debug(f"{method} {url} has received {data}")
                return data

            if response.status in {500, 503}:
                raise InternalServerError(response, data)

            if response.status == 401:
                raise AuthenticationError(response, data)
            elif response.status == 402:
                raise InsufficientFunds(response, data)
            elif response.status == 403:
                raise Forbidden(response, data)
            elif response.status == 404:
                raise NotFound(response, data)

    async def get_items(self, **parameters: Any):
        return await self.request(Route("GET", "/items"), **parameters)

    async def get_sales_history(self, **parameters: Any):
        return await self.request(Route("GET", "/sales/history"), **parameters)

    async def get_sales_out_of_stock(self, **parameters: Any):
        return await self.request(Route("GET", "/sales/out-of-stock"), **parameters)

    async def get_account_transactions(self, **parameters: Any):
        return await self.request(Route("GET", "/account/transactions"), **parameters)
