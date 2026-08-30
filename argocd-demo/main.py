import os
from fastapi import FastAPI, Response, status
app = FastAPI()
@app.get("/health")
async def health_check(response: Response):
    if os.getenv("HAS_BUG") == "true":
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"version":"v1", "status": "error"}
    return {"version": "v1","status": "ok"}
