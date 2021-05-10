import logging
import sys
from typing import List

from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret


API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Token"

VERSION = "1.0.0"

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)

PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI Proyecto Demo")

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO

LOGGERS = ("uvicorn.asgi", "uvicorn.access")

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

###
QUEEN: str = config("QUEEN",  default="")
AVAILABLE: str = config("AVAILABLE",  default="")
CLOSED: str = config("CLOSED",  default="")
###


logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
