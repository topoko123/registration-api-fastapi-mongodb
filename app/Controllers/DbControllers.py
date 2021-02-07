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

    def ApiList(self, page, limit, filter, order) :
        return self.db.ApiList(page, limit, filter, order,self.jsonout)
#=====================================================================================================#

    def MyApiList(self, page, limit, user_id, filter, order)  :
        return self.db.MyApiList(page, limit, user_id, filter, order,self.jsonout)
#=====================================================================================================#

    def SuperuserList(self, page, limit, user_id, status, filter, order) :
        return self.db.SuperuserList(page, limit, user_id, status, filter, order,self.jsonout)
#=====================================================================================================#

    def ServiceAdd(self, data):
        return self.db.ServiceAdd(data, self.jsonout)
#=====================================================================================================#

    def UserSignin(self, data) :
        return self.db.UserSignin(data, self.jsonout)
#=====================================================================================================#
    
    def UpdateService(self, data) :
        return self.db.UpdateService(data, self.jsonout)
#=====================================================================================================#

    def SuperuserUpdate(self, data) :
        return self.db.SuperuserUpdate(data, self.jsonout)
#=====================================================================================================#

    def DeleteService(self, data) :
        return self.db.DeleteService(data, self.jsonout)
#=====================================================================================================#

    def SuperuserDelete(self, service_id, user_id, status) :
        return self.db.SuperuserDelete(service_id, user_id, status, self.jsonout)
#=====================================================================================================#
