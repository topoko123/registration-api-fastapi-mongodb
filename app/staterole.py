from typing import Dict, NoReturn
import Database.Config.conn as connect

_services      = connect.db.service
_users         = connect.db.user

class UserRole :


    def SuperuserList(user_id, status) -> AssertionError :
        _state_user = _users.find({'user_id': user_id})
        
        assert _state_user.count() != 0, 'Id not found'
        assert _state_user[0]['status'] == status, 'You not permission!!'
#=====================================================================================================#

    def MyserviceUpdate(data: Dict) -> AssertionError :
        _state_service = _services.find({'service_id': data['service_id']})

        assert _state_service.count()       != 0, 'Service not found'
        assert _state_service[0]['user_id'] == data['user_id'], 'Id not found'
#=====================================================================================================#

    def SuperuserUpdate(data: Dict) -> AssertionError :
        _state_user = _users.find({'user_id': data['user_id']})

        assert _state_user.count()      != 0 , 'Id not found'
        assert _state_user[0]['status'] == data['status'], 'You not permission'
#=====================================================================================================#

    def MyserviceDel(data: Dict) -> AssertionError :
        _state_service = _services.find({'service_id': data['service_id']})

        assert _state_service.count()       != 0, 'Service not found'
        assert _state_service[0]['user_id'] == data['user_id'], 'Id not found'
#=====================================================================================================#

    def SuperuserDel(service_id: str, user_id: str, status: str) -> AssertionError :
        _state_user    = _users.find({'user_id': user_id})
        _state_service = _services.find({'service_id': service_id})

        assert _state_user.count()      != 0, 'Id not found'
        assert _state_user[0]['status'] == status, 'You not permission'
        assert _state_service.count()   != 0, 'Service not found'
#=====================================================================================================#
