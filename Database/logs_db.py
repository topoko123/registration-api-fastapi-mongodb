import Database.Config.conn as connect
from typing import Collection, Dict
#=====================================================================================================#
_users      = connect.db.user
_users_logs = connect.db.userlogs
_service_logs= connect.db.servicelogs
_update_logs = connect.db.updatelogs
_delete_logs = connect.db.deletelogs
#=====================================================================================================#

class Logs :

    def UserLogs(self, data: Dict) -> Collection[Dict] :   
        try:
            data_logs = {
                'gg': data['gg']['gmail'],
                'operation': 'create_user',
                'datetime' : data['datetime']
            }
        except Exception as e:
            print (e,(type,(e))) 
            data_logs = {'msg': 'Error'}                          #insert user_log collections
        return _users_logs.insert_one(data_logs)
#=====================================================================================================#

    def ServiceLogs(self, data: Dict) -> Collection[Dict] :                                #insert service_log collections
        try:
            data_logs = {}
            _state_user = _users.find({'user_id': data['user_id']})

            data_logs = {
                'gg': _state_user[0]['gg']['gmail'],
                'servuce_name': data['service_name'],
                'operation'   : 'create_service',
                'datetime'    : data['datetime']
            }
        except Exception as e:
            print(e,(type,(e)))
            data_logs = {'msg':'Error'}
        return _service_logs.insert_one(data_logs)
#=====================================================================================================#

    def UpdateLogs(self, data: Dict) -> Collection[Dict] :
        try:
            data_logs = {}
            _state_user= _users.find({'user_id': data['user_id']})

            data_logs = {
                'gg': _state_user[0]['gg']['gmail'],
                'service_name': data['service_name'],
                'operation'   : 'update_service',
                'datetime'    : data['datetime']
            }
        except Exception as e:
            print(e,(type,(e)))
            data_logs = {'msg':'Error'}
        return _update_logs.insert_one(data_logs)
#=====================================================================================================#

    def DeleteLogs(self, data: Dict) -> Collection[Dict] :
        try:
            data_logs = {}
            _state_user = _users.find({'user_id': data['user_id']})

            data_logs = {
                'gg': _state_user[0]['gg']['gmail'],
                'operation': 'delete_service',
                'datetime' : data['datetime']
            }
        except Exception as e:
            print(e,(type,(e)))
            data_logs = {'msg': 'Error'}
        return _delete_logs.insert_one(data_logs)
