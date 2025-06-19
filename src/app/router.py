import logging
import structlog
from litestar import Router, get



@get("/status")
async def status() -> dict:
    logging.getLogger(__name__).warning("status")
    structlog.get_logger(__name__).warning("status")
    return {"message": "Hello World!"}


app_router = Router("", route_handlers=[status])
