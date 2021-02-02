import os
from Database.crud_db import DB
from app.Service import Service
#=====================================================================================================#


class Controller :
    db = DB()
    newService = Service()
    jsonout    = {}
    param_name = []
    param_type = []
#=====================================================================================================#

    def Index(self):
        return self.newService.Index()
#=====================================================================================================#

    def ApiList(self, page, limit):
        return self.db.ApiList(page, limit, self.jsonout)
#=====================================================================================================#

    def MyApiList(self, page, limit, user_id):
        return self.db.MyApiList(page, limit, user_id, self.jsonout)
#=====================================================================================================#

    def SuperuserList(self, page, limit, user_id, status):
        return self.db.SuperuserList(page, limit, user_id, status, self.jsonout)
#=====================================================================================================#

    def ServiceAdd(self, data):
        return self.db.ServiceAdd(data, self.jsonout)
#=====================================================================================================#

    def UserSignin(self, data):
        return self.db.UserSignin(data, self.jsonout)
#=====================================================================================================#
    
    def UpdateService(self, data):
        return self.db.UpdateService(data, self.jsonout)
#=====================================================================================================#

    def SuperuserUpdate(self, data):
        return self.db.SuperuserUpdate(data, self.jsonout)
#=====================================================================================================#

    def DeleteService(self, data):
        return self.db.DeleteService(data, self.jsonout)
#=====================================================================================================#

    def SuperuserDelete(self, service_id, user_id, status):
        return self.db.SuperuserDelete(service_id, user_id, status, self.jsonout)
#=====================================================================================================#

    def Demo(self, data):
        return self.db.Demo(data)
        