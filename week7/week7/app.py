import logging
import os

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from starlette.middleware.sessions import SessionMiddleware

from week7.routers.login import router
from week7 import statics
from week7.setting import config as cnf

STATIC_PATH:os.PathLike = os.path.realpath(os.path.dirname(statics.__file__))



log = logging.getLogger()
app = FastAPI()



app.mount("/statics", StaticFiles(directory=STATIC_PATH), name="static")
app.include_router(router, )
app.add_middleware(SessionMiddleware, secret_key=cnf.SECRET_KEY)


