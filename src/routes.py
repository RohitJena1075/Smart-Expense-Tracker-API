from fastapi import APIRouter, HTTPException, Query, status

from src.schemas import (
    CategoryTotalExpense,
    Expense,
    ExpenseCreate,
    TotalExpense,
)
from src.storage import (
    add_expense,
    calculate_total,
    delete_expense,
    get_expenses,
)

router = APIRouter(tags=["Expenses"])


@router.post(
    "/expenses",
    response_model=Expense,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new expense",
)
def create_expense(expense: ExpenseCreate) -> Expense:
    """
    Create a new expense and store it.
    """

    saved_expense = add_expense(expense)
    return Expense(**saved_expense)


@router.get(
    "/expenses",
    response_model=list[Expense],
    summary="View expenses",
)
def list_expenses(
    category: str | None = Query(
        default=None,
        description="Filter expenses by category",
    ),
) -> list[Expense]:
    """
    Return all expenses or only expenses
    belonging to a specific category.
    """

    expenses = get_expenses(category)

    return [Expense(**expense) for expense in expenses]


@router.get(
    "/expenses/total",
    summary="Calculate expense totals",
)
def get_total(
    category: str | None = Query(
        default=None,
        description="Calculate total for a category",
    ),
) -> TotalExpense | CategoryTotalExpense:
    """
    Calculate the total amount spent.

    If a category is supplied,
    only that category is included.
    """

    total = calculate_total(category)

    if category is None:
        return TotalExpense(total=total)

    return CategoryTotalExpense(
        category=category,
        total=total,
    )


@router.delete(
    "/expenses/{expense_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete an expense",
)
def remove_expense(expense_id: int) -> dict[str, str]:
    """
    Delete an expense using its ID.
    """

    deleted = delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found.",
        )

    return {"message": "Expense deleted successfully."}