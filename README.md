# Smart Expense Tracker API

## Overview

This project is a REST API built using **FastAPI** to manage personal expenses. It allows users to add, view, filter, calculate totals, and delete expense records. To keep the project simple and aligned with the assignment requirements, expense data is stored in a local JSON file instead of using a database.

The project also includes automated tests using **pytest** and FastAPI's built-in **Swagger UI** for testing the API.

---

## Features

* Add a new expense
* View all expenses
* Filter expenses by category
* Calculate total expenses

  * Overall total
  * Category-wise total
* Delete an expense
* Store data in a local JSON file
* Automated tests using pytest
* Swagger/OpenAPI documentation

---

## Tech Stack

* Python 3.13.5
* FastAPI
* Uvicorn
* Pytest
* HTTPX

---

## Project Structure

```text
smart-expense-tracker/
│
├── data/
│   └── expenses.json
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── storage.py
│
├── tests/
│   ├── conftest.py
│   ├── test_create.py
│   ├── test_delete.py
│   ├── test_filter.py
│   ├── test_get.py
│   └── test_total.py
│
├── requirements.txt
├── README.md
└── AI_NOTES.md
```

---

## Prerequisites

Make sure the following are installed before running the project:

* Python 3.13.5
* pip

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Go to the project directory:

```bash
cd smart-expense-tracker
```

Create and activate a virtual environment (recommended).

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Server

Start the development server with:

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Once the server is running, open the following URL to access the Swagger UI:

```text
http://127.0.0.1:8000/docs
```

From there, you can test every endpoint directly in the browser.

---

## Running the Tests

Run the complete test suite using:

```bash
python -m pytest
```

The project includes automated tests for creating, retrieving, filtering, calculating totals, and deleting expenses.

---

## API Endpoints

| Method | Endpoint                              | Description                             |
| ------ | ------------------------------------- | --------------------------------------- |
| POST   | `/expenses`                           | Add a new expense                       |
| GET    | `/expenses`                           | View all expenses                       |
| GET    | `/expenses?category={category}`       | Filter expenses by category             |
| GET    | `/expenses/total`                     | Calculate total expenses                |
| GET    | `/expenses/total?category={category}` | Calculate total expenses for a category |
| DELETE | `/expenses/{expense_id}`              | Delete an expense                       |

---

## Example Request

```json
{
  "title": "Groceries",
  "amount": 1250.75,
  "category": "Food",
  "date": "2026-07-31"
}
```

---

## Data Storage

Expense data is stored in:

```text
data/expenses.json
```

No database setup is required.

---

## Bonus Feature

This project includes FastAPI's built-in **OpenAPI/Swagger documentation**, which makes it easy to test and explore all API endpoints.

---

## Notes

* Expense IDs are generated automatically.
* Input validation is handled using Pydantic.
* Tests use temporary JSON files, so they do not modify the actual application data.
* The project follows the folder structure specified in the assignment.
