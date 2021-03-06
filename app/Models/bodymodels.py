from pydantic import BaseModel
from typing import Optional, List



#=====================================================================================================#

class ServiceModel(BaseModel):
    service_name : str
    api_url      : str
    permission   : str
    user_id      : str
    description  : Optional[str] = None
    method       : str
    param_set    : list = []
#=====================================================================================================#

class UserModel(BaseModel):
    id_token    : str
    fullname    : str
    google_photo: str
    gmail       : str     
#=====================================================================================================#

class UserLineModel(BaseModel):
    access_token: str
    displayname : str
    ul_id       : str
    picture     : str
    id_li_tk    : str
#=====================================================================================================#


class ServiceDeleteModel(BaseModel):
    service_id : str
    user_id    : str
#=====================================================================================================#
    
class ServicePatchModel(BaseModel):
    service_name    : Optional[str] = None
    api_url         : Optional[str] = None
    permission      : Optional[str] = None
    service_id      : str
    description     : Optional[str] = None
    method          : Optional[str] = None
    param_set       : list = [] 
    user_id         : str
#=====================================================================================================#

class SuperUserPatchModel(BaseModel):
    service_id      : Optional[str] = None
    service_name    : Optional[str] = None
    api_url         : Optional[str] = None
    permission      : Optional[str] = None
    status          : Optional[str] = None
    description     : Optional[str] = None
    method          : Optional[str] = None
    param_set       : Optional[List] = []
    user_id         : Optional[str] = None
#=====================================================================================================#

class G_UserPatchModel(BaseModel):
    user_id     : str
    id_token    : str
    fullname    : str
    google_photo: str
    gmail       : str
#=====================================================================================================#

class L_UserPatchModel(BaseModel):
    user_id     : str
    access_token: str
    displayname : str
    ul_id       : str
    picture     : str
    id_li_tk    : str
#=====================================================================================================#


class SuperUserDeleteModel(BaseModel):
    service_id      : str
    user_id         : str
    status          : str
    


