import os
from Database.connection import DB
from app.Service import Service

class controller :
    db = DB()
    service = Service()


    def main(self):
        return self.service.get()

    def ListALl(self, page, limit):
        
        return self.db.ListALl(page, limit)

