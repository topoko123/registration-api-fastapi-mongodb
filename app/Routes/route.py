import os
from fastapi import APIRouter
from starlette.requests import Request
from app.Controllers.DbControllers import Controller
from app.Models.bodymodels import ServiceModel, UserModel, ServiceDeleteModel, ServicePatchModel
from app.Models.createmodels import createServer, createUser
#=====================================================================================================#

router = APIRouter()
newController = Controller()
#=====================================================================================================#

@router.get("/")
async def main():
    return newController.get()
#=====================================================================================================#     

@router.get("/service/list")
async def ApiList(page : int, limit: int):
    return newController.ApiList(page, limit)
#=====================================================================================================#

@router.get("/service/myapi/list")
async def MyApiList(page: int, limit: int, user_id: str):
    return newController.MyApiList(page, limit, user_id)
#=====================================================================================================#

@router.get("/service/superuser/list")
async def SuperuserList(page: int, limit: int, status: str):
    return newController.SuperuserList(page, limit, status)
#=====================================================================================================#

@router.post("/service/add-service")
async def ServiceAdd(serviceModels: ServiceModel):
    service_name = serviceModels.service_name
    api_url      = serviceModels.api_url.lower()
    permission   = serviceModels.permission.lower()
    user_id      = serviceModels.user_id
    description  = serviceModels.description
    method       = serviceModels.method
    param_name   = serviceModels.param_name
    param_type   = serviceModels.param_type
    desc         = serviceModels.desc
    
    data = createServer(service_name, api_url, permission, user_id, description, 
            method, param_name, param_type, desc)
    return newController.ServiceAdd(data)
#=====================================================================================================#

@router.post("/login")
async def UserSignin(userModels: UserModel):
    id_token      = userModels.id_token
    fullname      = userModels.fullname
    gmail         = userModels.gmail
    google_photo  = userModels.google_photo

    data = createUser(id_token, fullname, gmail, google_photo)
    return newController.UserSignin(data)
#=====================================================================================================#

# @router.patch("/service/myapi/update-service")
# async def UpdateService(updateServiceModels: ServicePatchModel):
    