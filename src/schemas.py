from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class ExpenseCreate(BaseModel):
    """
    Request body used to create a new expense.
    """

    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Expense title",
    )

    amount: float = Field(
        ...,
        gt=0,
        description="Expense amount",
    )

    category: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Expense category",
    )

    date: date


class Expense(ExpenseCreate):
    """
    Expense returned by the API.
    """

    id: int


class TotalExpense(BaseModel):
    """
    Response model for total expense calculations.
    """

    total: float


class CategoryTotalExpense(BaseModel):
    """
    Response model for category-wise totals.
    """

    category: str
    total: float