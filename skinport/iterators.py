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
from typing import Any, Callable, Coroutine, Dict, List, Optional, Union

from .transaction import Credit, Purchase, Withdraw


class TransactionAsyncIterator:
    def __init__(
        self,
        getter: Callable[..., Coroutine[Any, Any, Any]],
        limit: Optional[int] = None,
        pagination_token: int = 1,
        **kwargs: Dict[str, Any],
    ) -> None:
        self.limit = limit
        self.has_more = True
        self.getter = getter
        self.kwargs = kwargs

        self.transactions: asyncio.Queue[Union[Credit, Withdraw, Purchase]] = asyncio.Queue()
        self.previous_token = pagination_token
        self.next_token = pagination_token

    async def __anext__(self):
        try:
            return await self.next()
        except StopAsyncIteration as e:
            raise

    def __aiter__(self):
        return self

    async def flatten(self):
        return [element async for element in self]

    async def next(self) -> Union[Credit, Withdraw, Purchase]:
        if self.transactions.empty():
            await self.fill_transactions()

        try:
            return self.transactions.get_nowait()
        except asyncio.QueueEmpty as e:
            raise StopAsyncIteration from e

    async def fill_transactions(self):
        if not self.has_more:
            raise StopAsyncIteration

        data: Dict[str, Any] = await self.getter(params=self.kwargs)
        transactions: List[Dict[str, Any]] = data.get("data", [])

        for t in reversed(transactions):
            if t["type"] == "credit":
                self.transactions.put_nowait(Credit(data=t))
            elif t["type"] == "withdraw":
                self.transactions.put_nowait(Withdraw(data=t))
            elif t["type"] == "purchase":
                self.transactions.put_nowait(Purchase(data=t))

        self.previous_token = data["pagination"].get("page")
        self.next_token = data["pagination"].get("page") + 1
        self.kwargs["page"] = self.next_token

        if self.next_token > data["pagination"].get("pages"):
            self.has_more = False
