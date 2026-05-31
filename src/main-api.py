import socket
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from loguru import logger

from api.routers.v1 import router as router_v1
from constants import c


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.debug("Starting Server 🚀")
    yield
    logger.warning("Shutting down gracefully...")
    logger.warning("Cleanup complete. Server will now exit.")


app = FastAPI(
    title=c.title,
    description=c.description,
    summary="",
    terms_of_service="",
    docs_url="/docs",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/license/mit",
    },
    redoc_url=None,
    lifespan=lifespan,
)

app.include_router(router_v1)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time: float = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    client_host = request.client.host if request.client else "unknown"
    logger.debug(
        f"[{client_host}] Request: "
        f"{request.method} {request.url} - "
        f"Status: {response.status_code} - "
        f"Time: {process_time:.4f}s"
    )
    return response


@app.get("/ping")
async def ping() -> Response:
    """Test if the server is up and running"""
    return Response(content="pong!", media_type="text/plain")


@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!", "container_id": socket.gethostname()}
