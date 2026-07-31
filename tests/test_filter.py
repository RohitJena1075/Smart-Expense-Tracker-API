def test_filter_existing_category(client):
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
            "title": "Movie",
            "amount": 500,
            "category": "Entertainment",
            "date": "2026-07-29",
        },
    )

    response = client.get(
        "/expenses",
        params={"category": "food"},
    )

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_unknown_category(client):
    response = client.get(
        "/expenses",
        params={"category": "Medicine"},
    )

    assert response.status_code == 200
    assert response.json() == []