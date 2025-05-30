from litestar import Litestar


def create_app() -> Litestar:
    from litestar.di import Provide

    from app.config import get_config

    config = get_config()

    return Litestar(debug=config.app.debug, plugins=[])


asgi_application = create_app()
