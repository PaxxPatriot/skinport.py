import json
import unittest
from typing import List, Union

from skinport import Credit, Purchase, Withdraw

TEST_TRANSACTIONS = """{
    "pagination": {
        "page": 1,
        "pages": 1,
        "limit": 100,
        "order": "desc"
    },
    "data": [
        {
            "id": 9999993,
            "type": "credit",
            "sub_type": "item",
            "status": "complete",
            "amount": 1.57,
            "fee": 0.09,
            "currency": "EUR",
            "items": [
                {
                    "sale_id": 9999321,
                    "market_hash_name": "Mann Co. Supply Crate Key",
                    "seller_country": "DE",
                    "buyer_country": "DE"
                }
            ],
            "created_at": "2021-10-11T21:22:24.425Z",
            "updated_at": "2021-10-11T21:22:24.425Z"
        },
        {
            "id": 9999992,
            "type": "withdraw",
            "sub_type": null,
            "status": "complete",
            "amount": 1333.70,
            "fee": null,
            "currency": "EUR",
            "items": null,
            "created_at": "2021-10-11T05:30:10.880Z",
            "updated_at": "2021-10-11T06:14:07.427Z"
        },
        {
            "id": 9999991,
            "type": "purchase",
            "sub_type": null,
            "status": "complete",
            "amount": 90.01,
            "fee": null,
            "currency": "EUR",
            "items": [
                {
                    "sale_id": 9999123,
                    "market_hash_name": "★ Huntsman Knife",
                    "seller_country": "US",
                    "buyer_country": "DE"
                }
            ],
            "created_at": "2021-08-27T03:00:34.728Z",
            "updated_at": "2021-08-27T03:00:58.488Z"
        }
    ]
}"""


class TransactionTestCase(unittest.TestCase):
    def setUp(self):
        self._transactions = json.loads(TEST_TRANSACTIONS)

    def test_transaction_constructors(self):
        transactions: List[Union[Credit, Withdraw, Purchase]] = []
        for transaction in self._transactions["data"]:
            if transaction["type"] == "credit":
                transactions.append(Credit(data=transaction))
            elif transaction["type"] == "withdraw":
                transactions.append(Withdraw(data=transaction))
            elif transaction["type"] == "purchase":
                transactions.append(Purchase(data=transaction))
