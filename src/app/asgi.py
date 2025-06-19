from litestar import Litestar


def create_app() -> Litestar:
    from litestar.di import Provide

    from app.server import get_structlog_plugin
    from app.config import get_config
    from app.router import app_router

    config = get_config()

    return Litestar(
        route_handlers=[app_router],
        debug=config.app.debug,
        plugins=[get_structlog_plugin()],
        on_startup=[],
    )


asgi_application = create_app()
