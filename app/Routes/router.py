
from fastapi import APIRouter
from app.Routes.route import router 

api_router = APIRouter()
api_router.include_router(router,tags=["/api"],prefix=("/api"))