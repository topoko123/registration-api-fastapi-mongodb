import requests
from fastapi import Request, FastAPI, Depends, Body

class Service:
    
    def get(self):
        try:
            result = {'result': 'OK'}
        except:
            result = {'reuslt': 'Error'}
        return result
#=====================================================================================================#

    def ApiList(self, jsonout, total):
        return jsonout, total
#=====================================================================================================#

    def MyApiList(self, jsonout, total):
        return jsonout, total
#=====================================================================================================#

    def SuperuserList(self, jsonout, total):
        return jsonout, total
#=====================================================================================================#

    def ServiceAdd(self, jsonout):
        return jsonout
#=====================================================================================================#

    def UserSignin(self, jsonout):
        return jsonout