from typing import TypedDict


class ExpenseRecord(TypedDict):
    """
    Internal representation of an expense
    stored in the JSON file.
    """

    id: int
    title: str
    amount: float
    category: str
    date: str