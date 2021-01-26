from pydantic import BaseModel
from typing import Optional, List
import requests
from fastapi import Request, FastAPI

class ServiceModel(BaseModel):
    service_name : str
    api_url      : str
    permission   : str
    user_id      : str
    description  : Optional[str] = None
    method       : str
    param_name   : List[str] = []
    type         : Optional[str] = None
    desc         : Optional[str] = None

class UserModel(BaseModel):
    id_token    : str
    fullname    : str
    google_photo: str
    gmail       : str     


class ServiceDeleteModel(BaseModel):
    service_id : str
    user_id    : str
    

class ServicePatchModel(BaseModel):
    service_name    : Optional[str] = None
    api_url         : Optional[str] = None
    permission      : Optional[str] = None
    service_id      : str
    description     : Optional[str] = None
    method          : Optional[str] = None
    param_name      : List[str] = []
    type            : Optional[str] = None
    desc            : Optional[str] = None
    user_id         : str