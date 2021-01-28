import os
from fastapi import APIRouter
from starlette.requests import Request
from app.Controllers.DbControllers import Controller
from app.Models.bodymodels import ServiceModel, UserModel, ServiceDeleteModel, ServicePatchModel, SuperUserPatchModel
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

@router.post("/service/myapi/add-service")
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

@router.patch("/service/myapi/update-service")
async def UpdateService(updateServiceModels: ServicePatchModel):

    data = {
        'service_name' : updateServiceModels.service_name,
        'api_url'      : updateServiceModels.api_url,
        'permission'   : updateServiceModels.permission,
        'service_id'   : updateServiceModels.service_id,
        'description'  : updateServiceModels.description,
        'method'       : updateServiceModels.method,
        'param_name'   : updateServiceModels.param_name,
        'param_type'   : updateServiceModels.param_type,
        'desc'         : updateServiceModels.desc,
        'user_id'      : updateServiceModels.user_id
    }
    return newController.UpdateService(data)
#=====================================================================================================#

@router.patch("/service/superuser/update-service")
async def SuperuserUpdate(superuserUpdateModels: SuperUserPatchModel):
    
    data = {
        'service_name' : superuserUpdateModels.service_name,
        'api_url'      : superuserUpdateModels.api_url,
        'permission'   : superuserUpdateModels.permission,
        'service_id'   : superuserUpdateModels.service_id,
        'description'  : superuserUpdateModels.description,
        'method'       : superuserUpdateModels.method,
        'param_name'   : superuserUpdateModels.param_name,
        'param_type'   : superuserUpdateModels.param_type,
        'desc'         : superuserUpdateModels.desc,
        'status'       : superuserUpdateModels.status
    }
    return newController.SuperuserUpdate(data)
#=====================================================================================================#
@router.delete("/service/myapi/delete-service")
async def DeleteService(deleteServiceModels: ServiceDeleteModel):
    
    data = {
        'service_id': deleteServiceModels.service_id,
        'user_id'   : deleteServiceModels.user_id
    }
    return newController.DeleteService(data)