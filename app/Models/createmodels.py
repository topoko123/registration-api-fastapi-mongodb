from app.Models.db_models import ServiceModel, UserModel, UserLineModel
from bson import ObjectId
newService = ServiceModel()
newUser = UserModel()
newUserLine = UserLineModel()
# newDemo = DemoTest()
#=====================================================================================================#

#รับข้อมูลมาจาก main แล้วส่งไปยัง โมเดล
def createServer(service_name, api_url, permission, user_id, description, method, param_set):
    newService.Obj_id       = ObjectId()
    newService.service_name = service_name
    newService.api_url      = api_url
    newService.permission   = permission
    newService.user_id      = user_id
    newService.description  = description
    newService.method       = method
    newService.param_set    = param_set
    return dict(newService)
#=====================================================================================================#

def createUser(id_token, fullname, gmail, google_photo):
    newUser.Obj_id = ObjectId()
    newUser.gg     = { 'id_token': id_token, 'fullname': fullname, 'gmail': gmail, 'google_photo':google_photo}
    return dict(newUser)
#=====================================================================================================#

def createUserLine(access_token, displayname, ul_id, picture, _id_li_tk):
    newUserLine.Obj_id = ObjectId()
    newUserLine.ll = {
        'access_token': access_token,
        'displayname' : displayname,
        'ul_id'       : ul_id,
        'picture'     : picture,
        '_id_li_tk'   : _id_li_tk
    }
    return dict(newUserLine)
    