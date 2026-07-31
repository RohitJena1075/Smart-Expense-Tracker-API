def test_create_expense(client):
    response = client.post(
        "/expenses",
        json={
            "title": "Groceries",
            "amount": 850,
            "category": "Food",
            "date": "2026-07-30",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Groceries"
    assert data["amount"] == 850
    assert data["category"] == "Food"


def test_create_invalid_amount(client):
    response = client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": -50,
            "category": "Food",
            "date": "2026-07-30",
        },
    )

    assert response.status_code == 422


def test_create_missing_title(client):
    response = client.post(
        "/expenses",
        json={
            "amount": 100,
            "category": "Food",
            "date": "2026-07-30",
        },
    )

    assert response.status_code == 422