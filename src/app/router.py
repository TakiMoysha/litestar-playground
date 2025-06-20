from functools import lru_cache
import logging

from litestar.di import Provide
import structlog
from litestar import Router
from litestar import get


logger = logging.getLogger(__name__)


@get("/status")
async def status() -> dict:
    logging.getLogger(__name__).warning("status")
    structlog.get_logger(__name__).warning("status")
    return {"message": "Hello World!"}


@lru_cache
async def provide_rpc_client():
    client = {"connect": lambda: None}
    await client["connect"]()
    return client


@get("/rpc")
async def rpc_root(client=Provide(provide_rpc_client)) -> dict:
    logger.warning(f"rpc client: {str(client)}")
    return {"message": "Hello World!"}


app_router = Router("", route_handlers=[status])
