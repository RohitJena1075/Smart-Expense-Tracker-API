def test_total_expenses(client):
    client.post(
        "/expenses",
        json={
            "title": "Groceries",
            "amount": 500,
            "category": "Food",
            "date": "2026-07-30",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Taxi",
            "amount": 300,
            "category": "Transport",
            "date": "2026-07-29",
        },
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 800


def test_total_by_category(client):
    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-30",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Dinner",
            "amount": 450,
            "category": "Food",
            "date": "2026-07-29",
        },
    )

    response = client.get(
        "/expenses/total",
        params={"category": "Food"},
    )

    assert response.status_code == 200
    assert response.json()["total"] == 700