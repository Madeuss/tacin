from fastapi import APIRouter, FastAPI
from my_api.api.v1.api import api_router as api_v1_router
from my_api.api import healthcheck

def build_app() -> FastAPI:
    app = FastAPI(
        title="My FastAPI Project",
        description="This is a sample FastAPI project.",
        version="1.0.0",
    )
    router = APIRouter()

    router.include_router(api_v1_router, prefix="/api/v1")
    router.include_router(healthcheck.router, prefix="/api", tags=["Healthcheck"])

    app.include_router(router)

    return app



app: FastAPI = build_app()


