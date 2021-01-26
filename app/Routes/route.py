import os
from fastapi import APIRouter
from starlette.requests import Request
from app.Controllers.DbControllers import controller

router = APIRouter()
controller = controller()

@router.get("/")
async def main():
    return controller.get()

@router.get("/service/list")
async def ApiList(page : int, limit: int):
    return controller.ListALl(page, limit)
