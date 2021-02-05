from typing import Dict
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

    def ApiList(self, jsonout: Dict[str,str], total: Dict[str, int]) -> Dict:
        return jsonout, total
#=====================================================================================================#

    def MyApiList(self, jsonout: Dict[str,str], total: Dict[str, int]) -> Dict:
        return jsonout, total
#=====================================================================================================#

    def SuperuserList(self, jsonout: Dict[str,str], total: Dict[str, int]) -> Dict:
        return jsonout, total
#=====================================================================================================#

    def ServiceAdd(self, jsonout: Dict[str,str]) -> Dict:
        return jsonout
#=====================================================================================================#

    def UserSignin(self, jsonout: Dict[str,str]) -> Dict :
        return jsonout
#=====================================================================================================#

    def UpdateService(self, jsonout: Dict[str,str]) -> Dict :
        return jsonout
#=====================================================================================================#
    def SuperuserUpdate(self, jsonout: Dict[str,str]) -> Dict:
        return jsonout
#=====================================================================================================#

    def DeleteService(self, jsonout: Dict[str,str]) -> Dict:
        return jsonout
#=====================================================================================================#

    def SuperuserDelete(self, jsonout: Dict[str,str]) -> Dict:
        return jsonout
#=====================================================================================================#
