from pydantic import BaseModel, HttpUrl
from typing import Optional, List
import requests
from fastapi import Request, FastAPI


#=====================================================================================================#

class ServiceModel(BaseModel):
    service_name : str
    api_url      : str
    permission   : str
    user_id      : str
    description  : Optional[str] = None
    method       : str
    param_name   : List[str] = []
    param_type   : List[str] = []
    desc         : List[str] = []
#=====================================================================================================#

class UserModel(BaseModel):
    id_token    : str
    fullname    : str
    google_photo: str
    gmail       : str     
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
    param_name      : List[str] = []
    param_type      : List[str] = []
    desc            : List[str] = []
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
    param_name      : List[str] = []
    param_type      : List[str] = []
    desc            : List[str] = []
#=====================================================================================================#

class Demotest(BaseModel):
    service_name : str
    api_url      : str
    permission   : str
    user_id      : str
    description  : Optional[str] = None
    method       : str          
    param_set    : list = []
    


