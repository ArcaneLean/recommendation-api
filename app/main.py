"""Main entry point for the Recommendation API."""

from fastapi import FastAPI

app = FastAPI(title="Recommendation API")


@app.get("/")
def health_check() -> dict[str, str]:
    """Return a health status message."""
    return {"status": "ok"}
