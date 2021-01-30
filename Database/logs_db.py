import Database.Config.conn as connect
#=====================================================================================================#
_users      = connect.db.user
_users_logs = connect.db.userlogs
_service_logs= connect.db.servicelogs
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
            else:
                data_logs = {'msg': 'Not Found'}
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
            else:
                data_logs = {'msg' 'failed'}
        except Exception as e:
            print(e,(type,(e)))
            data_logs = 'Error'
        return _service_logs.insert_one(data_logs)
#=====================================================================================================#

