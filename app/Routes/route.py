from typing import Dict, Tuple

from fastapi import APIRouter

from app.Controllers.DbControllers import Controller

from app.Models.bodymodels import ServiceModel, UserModel, ServiceDeleteModel, ServicePatchModel, \
    SuperUserPatchModel, SuperUserDeleteModel, UserLineModel, G_UserPatchModel, L_UserPatchModel

from app.Models.createmodels import createServer, createUser, createUserLine 

#=====================================================================================================#

router = APIRouter()                
newController = Controller()

#=====================================================================================================#     

@router.get("/service/list")
async def ApiList(page : int, limit: int, filter: int) :
    return newController.ApiList(page, limit, filter)
#=====================================================================================================#

@router.get("/service/myapi/list")
async def MyApiList(page: int, limit: int, user_id: str, filter: int, public: int, private: int ) :
    return newController.MyApiList(page, limit, user_id, filter, public, private)
#=====================================================================================================#

@router.get("/service/superuser/list")
async def SuperuserList(page: int, limit: int, user_id: str, status: str, filter: int, public: int, private: int )  :
    return newController.SuperuserList(page, limit, user_id, status, filter, public, private)
#=====================================================================================================#

@router.post("/service/myapi/add-service")
async def ServiceAdd(serviceModels: ServiceModel) :
    service_name = serviceModels.service_name
    api_url      = serviceModels.api_url.lower()
    permission   = serviceModels.permission.lower()
    user_id      = serviceModels.user_id
    description  = serviceModels.description
    method       = serviceModels.method
    param_set    = serviceModels.param_set
    
    data = createServer(service_name, api_url, permission, user_id, description, 
            method, param_set)
    return newController.ServiceAdd(data)
#=====================================================================================================#

@router.post("/login")
async def UserSignin(userModels: UserModel) :
    id_token      = userModels.id_token
    fullname      = userModels.fullname
    gmail         = userModels.gmail
    google_photo  = userModels.google_photo

    data = createUser(id_token, fullname, gmail, google_photo)
    return newController.UserSignin(data)
#=====================================================================================================#

@router.post("/linelogin")
async def LineSingin(userLineModels: UserLineModel):
    access_token = userLineModels.access_token
    displayname = userLineModels.displayname
    ul_id       = userLineModels.ul_id
    picture     = userLineModels.picture
    id_li_tk    = userLineModels.id_li_tk

    data = createUserLine(access_token, displayname, ul_id, picture, id_li_tk)
    return newController.LineSignin(data)
#=====================================================================================================#


@router.patch("/service/myapi/update-service")
async def UpdateService(updateServiceModels: ServicePatchModel) :

    data = {
        'service_name' : updateServiceModels.service_name,
        'api_url'      : updateServiceModels.api_url,
        'permission'   : updateServiceModels.permission,
        'service_id'   : updateServiceModels.service_id,
        'description'  : updateServiceModels.description,
        'method'       : updateServiceModels.method,
        'param_set'    : updateServiceModels.param_set,
        'user_id'      : updateServiceModels.user_id
    }
    return newController.UpdateService(data)
#=====================================================================================================#

@router.patch("/service/superuser/update-service")
async def SuperuserUpdate(superuserUpdateModels: SuperUserPatchModel) :
    
    data = {
        'service_name' : superuserUpdateModels.service_name,
        'api_url'      : superuserUpdateModels.api_url,
        'permission'   : superuserUpdateModels.permission,
        'service_id'   : superuserUpdateModels.service_id,
        'description'  : superuserUpdateModels.description,
        'method'       : superuserUpdateModels.method,
        'param_set'    : superuserUpdateModels.param_set,
        'status'       : superuserUpdateModels.status,
        'user_id'      : superuserUpdateModels.user_id
    }
    return newController.SuperuserUpdate(data)
#=====================================================================================================#

@router.patch("/add-acc/gg-ll")
async def GG_add_Line(l_UserPatchModels: L_UserPatchModel):

    data = {
        'user_id' : l_UserPatchModels.user_id,
        'access_token': l_UserPatchModels.access_token,
        'displayname': l_UserPatchModels.displayname,
        'ul_id'      : l_UserPatchModels.ul_id,
        'picture'    : l_UserPatchModels.picture,
        'id_li_tk'   : l_UserPatchModels.id_li_tk
    }
    return newController.GG_add_Line(data)
#=====================================================================================================#

@router.patch("/add-acc/ll-gg")
async def LL_add_gg(g_UserPatchModels: G_UserPatchModel):
    data = {
        'user_id' : g_UserPatchModels.user_id,
        'id_token': g_UserPatchModels.id_token,
        'fullname': g_UserPatchModels.fullname,
        'gmail'   : g_UserPatchModels.gmail,
        'google_photo': g_UserPatchModels.google_photo
    }
    return newController.LL_add_gg(data)
#=====================================================================================================#


@router.delete("/service/myapi/delete-service")
async def DeleteService(deleteServiceModels: ServiceDeleteModel) :
    
    data = {
        'service_id': deleteServiceModels.service_id,
        'user_id'   : deleteServiceModels.user_id
    }
    return newController.DeleteService(data)
#=====================================================================================================#

@router.delete("/service/superuser/delete-service")
async def SuperuserDelete(superuserDelModels: SuperUserDeleteModel) :
    data = {
        'service_id': superuserDelModels.service_id,
        'user_id'   : superuserDelModels.user_id,
        'status'    : superuserDelModels.status
    }
    return newController.SuperuserDelete(data)
#=====================================================================================================#


