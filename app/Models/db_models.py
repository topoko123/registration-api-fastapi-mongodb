from schematics.models import Model
from schematics.types import StringType, URLType
from bson import ObjectId
#=====================================================================================================#

class ServiceModel(Model):
    Obj_id       = ObjectId()
    service_name = StringType(required=True)
    api_url      = URLType(required=True)
    permission   = StringType(required=True)
    user_id      = StringType(required=True)
    description  = StringType()
    method       = StringType(required=True)
    param_set    = StringType(required=True)
#=====================================================================================================#

class UserModel(Model):
    Obj_id = ObjectId()
    gg     = StringType(required=True)
    status = StringType(default='user')
#=====================================================================================================#
