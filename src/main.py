from fastapi import FastAPI

app = FastAPI(
    title="Smart Expense Tracker API",
    description="REST API for managing personal expenses.",
    version="1.0.0",
)


@app.get("/")
def root() -> dict[str, str]:
    """
    Health check endpoint.
    """
    return {"message": "Smart Expense Tracker API is running."}