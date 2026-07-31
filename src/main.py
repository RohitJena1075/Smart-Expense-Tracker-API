from fastapi import FastAPI

from src.routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    description=(
        "REST API for managing personal expenses."
    ),
    version="1.0.0",
)

app.include_router(router)


@app.get(
    "/",
    tags=["Health"],
    summary="Health check",
)
def health_check() -> dict[str, str]:
    """
    Verify that the API is running.
    """

    return {
        "message": "Smart Expense Tracker API is running."
    }