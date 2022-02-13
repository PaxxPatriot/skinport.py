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

from skinport.transaction import Transaction

from .errors import NoMoreItems


class TransactionAsyncIterator:
    def __init__(self, getter, limit=None, pagination_token=1, *args, **kwargs):
        self.limit = limit
        self.transactions = asyncio.Queue()
        self.has_more = True
        self.getter = getter
        self.kwargs = kwargs

        self.previous_token = pagination_token
        self.next_token = pagination_token

    async def __anext__(self):
        try:
            return await self.next()
        except NoMoreItems as e:
            raise StopAsyncIteration from e

    def __aiter__(self):
        return self

    async def flatten(self):
        return [element async for element in self]

    async def next(self) -> Transaction:
        if self.transactions.empty():
            await self.fill_transactions()

        try:
            return self.transactions.get_nowait()
        except asyncio.QueueEmpty as e:
            raise NoMoreItems from e

    async def fill_transactions(self):
        if not self.has_more:
            raise NoMoreItems

        data = await self.getter()
        transactions = data.get("data")

        for t in reversed(transactions):
            self.transactions.put_nowait(Transaction(data=t))

        self.previous_token = data["pagination"].get("page")
        self.next_token = data["pagination"].get("page") + 1
        self.kwargs["page"] = self.next_token

        if self.next_token >= data["pagination"].get("pages"):
            self.has_more = False