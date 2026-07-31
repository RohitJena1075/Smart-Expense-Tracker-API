import json
import os
from pathlib import Path

from src.models import ExpenseRecord
from src.schemas import ExpenseCreate


def get_data_file() -> Path:
    """
    Determine the path to the expenses JSON file at runtime.
    This reads `EXPENSE_DATA_FILE` from the environment on every call so
    tests that monkeypatch the environment get an isolated file path.
    """

    return Path(
        os.getenv(
            "EXPENSE_DATA_FILE",
            Path(__file__).resolve().parent.parent / "data" / "expenses.json",
        )
    )


def load_expenses() -> list[ExpenseRecord]:
    """
    Load all expenses from the JSON file.
    Returns an empty list if the file does not exist.
    Raises ValueError if the JSON content is invalid.
    """

    data_file = get_data_file()

    if not data_file.exists():
        return []

    try:
        with data_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("Expense data must be a list.")

            return data

    except json.JSONDecodeError as exc:
        raise ValueError("Expense data file contains invalid JSON.") from exc


def save_expenses(expenses: list[ExpenseRecord]) -> None:
    """
    Save all expenses to the JSON file.
    """

    data_file = get_data_file()
    data_file.parent.mkdir(parents=True, exist_ok=True)

    with data_file.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def get_next_id(expenses: list[ExpenseRecord]) -> int:
    """
    Generate the next available expense ID.
    """

    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1


def add_expense(expense_data: ExpenseCreate) -> ExpenseRecord:
    """
    Create a new expense, assign an ID,
    save it, and return the stored record.
    """

    expenses = load_expenses()

    expense: ExpenseRecord = {
        "id": get_next_id(expenses),
        "title": expense_data.title,
        "amount": expense_data.amount,
        "category": expense_data.category,
        "date": expense_data.date.isoformat(),
    }

    expenses.append(expense)
    save_expenses(expenses)

    return expense


def delete_expense(expense_id: int) -> bool:
    """
    Delete an expense by ID.

    Returns True if deleted.
    Returns False if the expense does not exist.
    """

    expenses = load_expenses()

    updated_expenses = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        return False

    save_expenses(updated_expenses)
    return True


def get_expenses(category: str | None = None) -> list[ExpenseRecord]:
    """
    Return all expenses or only those matching a category.
    """

    expenses = load_expenses()

    if category is None:
        return expenses

    category = category.strip().lower()

    return [
        expense
        for expense in expenses
        if expense["category"].lower() == category
    ]


def calculate_total(category: str | None = None) -> float:
    """
    Calculate total expenses.

    If a category is supplied,
    only expenses from that category are included.
    """

    expenses = get_expenses(category)

    return round(
        sum(expense["amount"] for expense in expenses),
        2,
    )