from .api import laboratory

from fastapi import FastAPI
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from .core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION

from starlette import requests
from starlette.responses import JSONResponse


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(laboratory.router, tags=[
                               "laboratory"], prefix=API_PREFIX)

    @application.get("/")
    def read_root():
        return {"Hello": "World"}

    return application


app = get_application()
