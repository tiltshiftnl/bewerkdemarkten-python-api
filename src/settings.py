import os
from typing import List, Union
import json

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    REPOSITORY_DIR = os.environ.get(
        'REPOSITORY_DIR', "/tmp/bewerkdemarkten-repo")
    PDF_DIR = os.environ.get('PDF_DIR', f"{REPOSITORY_DIR}dist/pdf/")
    JSON_DIR = os.environ.get('JSON_DIR', f"{REPOSITORY_DIR}/config/markt/")

    GIT_REPOSITORY = os.environ.get(
        'GIT_REPOSITORY', "https://github.com/Amsterdam/fixxx-pakjekraam.git")
    DATABASE_URL = os.environ.get(
        'DATABASE_URL', "postgresql://postgres:postgres@localhost/postgres")
    USERS = json.loads(os.environ.get('USERS', '{"demo": "test12345"}'))
    BACKEND_CORS_ORIGINS_CSV: str = os.environ.get(
        'BACKEND_CORS_ORIGINS_CSV', "http://localhost,http://localhost:4200,http://localhost:3000")


settings = Settings()
