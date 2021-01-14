import os
from typing import List, Union
import json

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    GIT_REPOSITORY = os.environ.get('GIT_REPOSITORY', "https://github.com/Amsterdam/fixxx-pakjekraam.git")
    DATABASE_URL = os.environ.get('DATABASE_URL', "postgresql://postgres:postgres@localhost/postgres")
    USERS = json.loads(os.environ.get('USERS', '{"demo": "test12345"}'))
    BACKEND_CORS_ORIGINS_CSV: str = os.environ.get('BACKEND_CORS_ORIGINS_CSV', "http://localhost,http://localhost:4200,http://localhost:3000")

settings = Settings()
