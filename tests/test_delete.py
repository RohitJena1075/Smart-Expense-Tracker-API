def test_delete_existing_expense(client):
    client.post(
        "/expenses",
        json={
            "title": "Groceries",
            "amount": 500,
            "category": "Food",
            "date": "2026-07-30",
        },
    )

    response = client.delete("/expenses/1")

    assert response.status_code == 200


def test_delete_missing_expense(client):
    response = client.delete("/expenses/999")

    assert response.status_code == 404