import requests
import fastapi
from starlette import responses
#=====================================================================================================#

class Service:
    
    def Index():
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
#=====================================================================================================#

    def UpdateService(self, jsonout):
        return jsonout
#=====================================================================================================#
    def SuperuserUpdate(self, jsonout):
        return jsonout
#=====================================================================================================#

    def DeleteService(self, jsonout):
        return jsonout
#=====================================================================================================#

    def SuperuserDelete(self, jsonout):
        return jsonout
#=====================================================================================================#
