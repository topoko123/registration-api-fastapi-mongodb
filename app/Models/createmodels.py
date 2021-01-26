from app.Models.db_models import ServiceModel, UserModel
from bson import ObjectId
newService = ServiceModel()
newUser = UserModel()

#รับข้อมูลมาจาก main แล้วส่งไปยัง โมเดล
def createServer(service_name, api_url, permission, description, user_id, method, param_name, type, desc):
    newService.Obj_id       = ObjectId()
    newService.service_name = service_name
    newService.api_url      = api_url
    newService.permission   = permission
    newService.method       = method
    newService.description  = description
    newService.param_set    = {'param_name': param_name, 'type': type, 'desc': desc}
    newService.user_id      = user_id

    return dict(newService)

def createUser(id_token, fullname, gmail, google_photo):

    newUser.Obj_id = ObjectId()
    newUser.gg     = { 'id_token': id_token, 'fullname': fullname, 'gmail': gmail, 'google_photo':google_photo}

    return dict(newUser)


