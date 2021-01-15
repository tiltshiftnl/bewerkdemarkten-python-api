from fastapi import FastAPI, Request, Response
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware
from .generic import v1 as generic_v1
from .market import v1 as market_v1
from .database import SessionLocal
from .settings import settings
from .git import Git

app = FastAPI()
Git.clone()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Bewerkdemarkten-api",
        version="0.8.1",
        description="This is the API for Bewerkdemarkten",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS_CSV.split(','),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers moved to individual files in the ./routers folder
app.include_router(generic_v1.router)
app.include_router(market_v1.router)
app.openapi = custom_openapi