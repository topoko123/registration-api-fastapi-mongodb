import os
from Database.connection import DB
from app.Service import Service


class Controller :
    db = DB()
    newService = Service()
    jsonout    = {}
#=====================================================================================================#

    def main(self):
        return self.newService.get()
#=====================================================================================================#

    def ApiList(self, page, limit):
        return self.db.ApiList(page, limit, self.jsonout)
#=====================================================================================================#

    def MyApiList(self, page, limit, user_id):
        return self.db.MyApiList(page, limit, user_id, self.jsonout)
#=====================================================================================================#

    def SuperuserList(self, page, limit, status):
        return self.db.SuperuserList(page, limit, status, self.jsonout)
#=====================================================================================================#

    def ServiceAdd(self, data):
        return self.db.ServiceAdd(data, self.jsonout)
#=====================================================================================================#

    def UserSignin(self, data):
        return self.db.UserSignin(data, self.jsonout)
    


        