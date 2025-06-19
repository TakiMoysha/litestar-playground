import logging
import logging.config
from litestar.logging.config import LoggingConfig
from litestar.plugins.structlog import StructlogConfig, StructLoggingConfig, StructlogPlugin


LOG_LEVEL = "DEBUG"


def get_structlog_plugin():
    # LOGGING_CONFIG = {
    # "handlers": {
    #     "default": {
    #         "formatter": "default",
    #         "class": "logging.StreamHandler",
    #         "stream": "ext://sys.stdout",  # stderr
    #     },
    # },
    # }
    # logging.config.dictConfig(LOGGING_CONFIG)

    structlog_plugin = StructlogPlugin(
        config=StructlogConfig(
            structlog_logging_config=StructLoggingConfig(
                standard_lib_logging_config=LoggingConfig(
                    root={
                        "level": LOG_LEVEL,
                        "handlers": ["console", "rotated_file"],
                    },
                    handlers={
                        "rotated_file": {
                            "class": "logging.handlers.RotatingFileHandler",
                            "filename": "tmp/litestar.log",
                            "maxBytes": 10 * 1024 * 1024,
                            "backupCount": 10,
                            "formatter": "standard",
                        },
                    },
                ),
            )
        )
    )

    return structlog_plugin
