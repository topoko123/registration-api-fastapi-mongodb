import Database.Config.conn as connect
#=====================================================================================================#
_users      = connect.db.user
_users_logs = connect.db.userlogs
_service_logs= connect.db.servicelogs
_update_logs = connect.db.updatelogs
_delete_logs = connect.db.deletelogs
#=====================================================================================================#

class Logs :

    def UserLogs(self, data):   
        try:
            for find in data:
                data_logs = {
                    'gg': find['gg']['gmail'],
                    'operation': 'create_user',
                    'datetime' : find['datetime']
                }
                break
        except Exception as e:
            print (e,(type,(e))) 
            data_logs = {'msg': 'Error'}                          #insert user_log collections
        return _users_logs.insert_one(data_logs)
#=====================================================================================================#

    def ServiceLogs(self, data):                                #insert service_log collections
        try:
            data_logs = {}
            for find in _users.find({'user_id': data['user_id']}):
                data_logs = {
                    'gg': find['gg']['gmail'],
                    'service_name': data['service_name'],
                    'operation'   : 'create_service',
                    'datetime'    : data['datetime']
                }
                break

        except Exception as e:
            print(e,(type,(e)))
            data_logs = {'msg':'Error'}
        return _service_logs.insert_one(data_logs)
#=====================================================================================================#

    def UpdateLogs(self, data):
        try:
            data_logs = {}
            for find in _users.find({'user_id': data['user_id']}):
                data_logs = {
                    'gg': find['gg']['gmail'],
                    'service_name': data['service_name'],
                    'operation'   : 'update_service',
                    'datetime'    : data['datetime']
                }
        except Exception as e:
            print(e,(type,(e)))
            data_logs = {'msg':'Error'}
        return _update_logs.insert_one(data_logs)
#=====================================================================================================#

    def DeleteLogs(self, data):
        try:
            for find in _users.find({'user_id': data['user_id']}):
                data_logs = {
                    'gg': find['gg']['gmail'],
                    'operation': 'delete_service',
                    'datetime' : data['datetime']
                }
        except Exception as e:
            print(e,(type,(e)))
            data_logs = {'msg': 'Error'}
        return _delete_logs.insert_one(data_logs)
