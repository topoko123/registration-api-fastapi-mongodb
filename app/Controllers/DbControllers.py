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

    def ApiList(self, page, limit, filter) :
        return self.db.ApiList(page, limit, filter,self.jsonout)
#=====================================================================================================#

    def MyApiList(self, page, limit, user_id, filter, public, private) :
        if public and private == 1:
            return self.db.MyApiList_All(page, limit, user_id, filter, self.jsonout)
        elif public == 1:
            return self.db.MyApiList_Public(page, limit, user_id, filter, self.jsonout)
        else:
            return self.db.MyApiList_private(page, limit, user_id, filter, self.jsonout)
#=====================================================================================================#

    def SuperuserList(self, page, limit, user_id, status, filter, public, private) :
        if public and private == 1:
            return self.db.SuperuserList_All(page, limit, user_id, status, filter, self.jsonout)
        elif public == 1:
            return self.db.SuperuserList_Public(page, limit, user_id, status, filter, self.jsonout)
        else:
            return self.db.SuperuserList_Private(page, limit, user_id, status, filter, self.jsonout)
#=====================================================================================================#

    def ServiceAdd(self, data):
        return self.db.ServiceAdd(data, self.jsonout)
#=====================================================================================================#

    def UserSignin(self, data) :
        return self.db.UserSignin(data, self.jsonout)
#=====================================================================================================#

    def LineSignin(self, data):
        return self.db.LineSignin(data, self.jsonout)
#=====================================================================================================#
    
    def UpdateService(self, data) :
        return self.db.UpdateService(data, self.jsonout)
#=====================================================================================================#

    def SuperuserUpdate(self, data) :
        return self.db.SuperuserUpdate(data, self.jsonout)
#=====================================================================================================#
    def GG_add_Line(self, data):
        return self.db.GG_add_Line(data, self.jsonout)
#=====================================================================================================#
    def LL_add_gg(self, data):
        return self.db.LL_add_gg(data, self.jsonout)
#=====================================================================================================#


    def DeleteService(self, data) :
        return self.db.DeleteService(data, self.jsonout)
#=====================================================================================================#

    def SuperuserDelete(self, data) :
        return self.db.SuperuserDelete(data, self.jsonout)
#=====================================================================================================#
