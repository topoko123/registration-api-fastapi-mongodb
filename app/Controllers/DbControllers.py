import os
from typing import Dict, Tuple
from Database.crud_db import DB
from app.Service import Service
#=====================================================================================================#


class Controller :
    db = DB()
    newService = Service()
    jsonout    = {}

#=====================================================================================================#

    def Index(self):
        return self.newService.Index()
#=====================================================================================================#

    def ApiList(self, page: int, limit: int) -> Tuple[int, int, Dict]:
        return self.db.ApiList(page, limit, self.jsonout)
#=====================================================================================================#

    def MyApiList(self, page: int, limit: int, user_id: str) -> Tuple[int, int, str, Dict] :
        return self.db.MyApiList(page, limit, user_id, self.jsonout)
#=====================================================================================================#

    def SuperuserList(self, page: int, limit: int, user_id: str, status: str) -> Tuple[int, int, str, str, Dict] :
        return self.db.SuperuserList(page, limit, user_id, status, self.jsonout)
#=====================================================================================================#

    def ServiceAdd(self, data: Dict[str,str]) -> Dict[str, str]:
        return self.db.ServiceAdd(data, self.jsonout)
#=====================================================================================================#

    def UserSignin(self, data: Dict[str,str]) -> Dict[str, str]:
        return self.db.UserSignin(data, self.jsonout)
#=====================================================================================================#
    
    def UpdateService(self, data: Dict[str,str]) -> Dict[str, str]:
        return self.db.UpdateService(data, self.jsonout)
#=====================================================================================================#

    def SuperuserUpdate(self, data: Dict[str,str]) -> Dict[str, str]:
        return self.db.SuperuserUpdate(data, self.jsonout)
#=====================================================================================================#

    def DeleteService(self, data: Dict[str,str]) -> Dict[str, str]:
        return self.db.DeleteService(data, self.jsonout)
#=====================================================================================================#

    def SuperuserDelete(self, service_id: str, user_id: str, status: str) -> Tuple[str, str, str] :
        return self.db.SuperuserDelete(service_id, user_id, status, self.jsonout)
#=====================================================================================================#
