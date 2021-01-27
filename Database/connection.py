import os
import Database.Config.conn as connec
from pymongo import MongoClient
from app.Service import Service

sv = Service()

class DB:

    def ListALl(self, page, limit, jsonout):
        
        total   = {}
        startat = (page - 1) * limit
        
        try:        
            for find in connec.db.service.find({'permission': 'public'}, {'unix_time': 0}).skip(startat).limit(limit):
                for search in connec.db.user.find({'user_id': find['user_id']}, {'unix_time': 0, 'gg.id_token': 0}):
                    service_id = find['service_id']
                    dict = {
                        'service_id'  : service_id,
                        'service_name': find.get('service_name'),
                        'api_url'     : find.get('api_url'),
                        'permission'  : find.get('permission'),
                        'description' : find.get('description'),
                        'method'      : find.get('method'),
                        'param_name'  : find['param_set']['param_name'],
                        'type'        : find['param_set']['type'],
                        'desc'        : find['param_set']['desc'],
                        'user_id'     : find.get('user_id'),
                        'gmail'       : search['gg']['gmail'],
                        'datetime'    : find.get('datetime')
                    }
                    jsonout[service_id] = dict
            # sd = connec.db.user.count()
        except Exception as e:
            print (e, (type,(e)))
        
        return sv.ListALll(jsonout)



