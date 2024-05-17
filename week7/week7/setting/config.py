import os

from dotenv import load_dotenv

load_dotenv()

_env = os.environ


HOST = _env.get("MYSQL_HOST", 'localhost')
USER = _env.get("MYSQL_USERNAME", 'root')
PASSWORD = _env.get("MYSQL_PASSWORD", None)
DATABASE = _env.get("MYSQL_DATABASE", 'website')
SECRET_KEY = _env.get("SECRET_KEY", None)