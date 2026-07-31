def test_get_all_expenses(client):
    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 500,
            "category": "Food",
            "date": "2026-07-30",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Metro",
            "amount": 300,
            "category": "Transport",
            "date": "2026-07-29",
        },
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_empty_expenses(client):
    response = client.get("/expenses")

    assert response.status_code == 200
    assert response.json() == []