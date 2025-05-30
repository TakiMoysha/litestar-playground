from dataclasses import dataclass, field
from functools import lru_cache


@dataclass
class AppConfig:
    debug: bool = field(default=False)


@dataclass
class Config:
    app: AppConfig = field(default_factory=AppConfig)


@lru_cache(maxsize=1, typed=True)
def get_config() -> Config:
    return Config()
