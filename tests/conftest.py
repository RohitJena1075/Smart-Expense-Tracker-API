import json
import os

import pytest
from fastapi.testclient import TestClient



@pytest.fixture
def client(tmp_path, monkeypatch):
    """
    Create an isolated JSON file for every test.
    """

    data_file = tmp_path / "expenses.json"
    data_file.write_text("[]", encoding="utf-8")

    monkeypatch.setenv(
        "EXPENSE_DATA_FILE",
        str(data_file),
    )
    from src.main import app


    return TestClient(app)