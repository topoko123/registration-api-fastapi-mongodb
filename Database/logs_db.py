import Database.Config.conn as connect
#=====================================================================================================#
_users      = connect.db.user
_users_logs = connect.db.userlogs
_service_logs= connect.db.servicelogs
#=====================================================================================================#


class Logs :

    def UserLogs(self, data):                                   #insert user_log collections
        data['operation'] = 'create_user'
        return _users_logs.insert_one(data)
#=====================================================================================================#

    def ServiceLogs(self, data):                                #insert service_log collections
        try:
            for find in _users.find({'user_id': data['user_id']}):
                data['gg'] = find['gg']['gmail']
                data['operation'] = 'create_service'
                break
        except Exception as e:
            print(e,(type,(e)))
        return _service_logs.insert_one(data)
#=====================================================================================================#

