from typing import Dict
import requests
import fastapi
from starlette import responses
#=====================================================================================================#

class Service:
    
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

    def LineSignin(self, jsonout: Dict[str, str]) -> Dict:
        return jsonout
#=====================================================================================================#

    def UpdateService(self, jsonout: Dict[str,str]) -> Dict :
        return jsonout
#=====================================================================================================#
    def SuperuserUpdate(self, jsonout: Dict[str,str]) -> Dict:
        return jsonout
#=====================================================================================================#
    def GG_add_Line(self, jsonout: Dict[str, str]) -> Dict:
        return jsonout
#=====================================================================================================#

    def LL_add_gg(self, jsonout: Dict[str, str]) -> Dict:
        return jsonout
#=====================================================================================================#

    def DeleteService(self, jsonout: Dict[str,str]) -> Dict:
        return jsonout
#=====================================================================================================#

    def SuperuserDelete(self, jsonout: Dict[str,str]) -> Dict:
        return jsonout
#=====================================================================================================#
    def MyApiList_null():
        return 0