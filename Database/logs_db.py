import Database.Config.conn as connect
#=====================================================================================================#

_users_logs = connect.db.userlogs
_service_logs= connect.db.servicelogs
#=====================================================================================================#


class Logs :

    def UserLogs(self, data):                                   #insert user_log collections
        data['operation'] = 'create_user'
        return _users_logs.insert(data)
#=====================================================================================================#

    def ServiceLogs(self, data):                                #insert service_log collections
        data['operation'] = 'create_service'
        return _service_logs.insert(data)
#=====================================================================================================#

