import os
from typing import List

from pymongo.results import InsertOneResult
from Database.logs_db import Logs
import Database.Config.conn as connect
from app.Service import Service
from hashlib import sha256
import time
import datetime
#=====================================================================================================#

_services      = connect.db.service
_users         = connect.db.user
# _demo          = connect.db.demo
#=====================================================================================================#

class DB:
    newLogs    = Logs()
    newService = Service()
    total      = {}
#=====================================================================================================#

    def ApiList(self, page, limit, jsonout): 
        try:        
            jsonout = {}

            startat = (page - 1) * limit
            for find in _services.find({'permission': 'public'}, 
                    {'unix_time': 0}).skip(startat).limit(limit):
                for search in _users.find({'user_id': find['user_id']}, 
                    {'unix_time': 0, 'gg.id_token': 0}):

                    service_id = find['service_id']
                    dict = {
                        'service_id'  : service_id,
                        'service_name': find['service_name'],
                        'api_url'     : find['api_url'],
                        'permission'  : find['permission'],
                        'description' : find['description'],
                        'method'      : find['method'],
                        'param_name'  : find['param_set']['param_name'],
                        'param_type'  : find['param_set']['param_type'],
                        'desc'        : find['param_set']['desc'],
                        'gmail'       : search['gg']['gmail'],
                        'datetime'    : find['datetime']
                    }
                    jsonout[service_id] = dict
            self.total['total'] = _services.count({'permission': 'public'})
        except Exception as e:
            print (e, (type,(e)))

        return self.newService.ApiList(jsonout, self.total)
#=====================================================================================================#

    def MyApiList(self, page, limit, user_id, jsonout):
        try:
            jsonout = {}
            startat = (page - 1) * limit
            for find in _services.find({'user_id': user_id}).skip(startat).limit(limit):
                for search in _users.find({'user_id': find['user_id']}, {'unix_time': 0, 'gg.id_token': 0}):

                    service_id = find['service_id']            
                    dict = {
                        'service_id'  : service_id,
                        'service_name': find['service_name'],
                        'api_url'     : find['api_url'],
                        'permission'  : find['permission'],
                        'description' : find['description'],
                        'method'      : find['method'],
                        'param_set'   : find['param_set'],
                        'datetime'    : find['datetime']
                    }
                    jsonout[service_id] = dict
                   
                    
            self.total['total'] = _services.count({'user_id': user_id})
        except Exception as e:
            print(e, (type, (e)))

        return self.newService.MyApiList(jsonout, self.total)
#=====================================================================================================#

    def SuperuserList(self, page, limit, status, jsonout):
        try:
            jsonout = {}
            startat = (page - 1) * limit
            if status == 'superuser':
                for find in _services.find().skip(startat).limit(limit):
                    for search in _users.find({'user_id': find['user_id']}, {'unix_time': 0, 'gg.id_token': 0}):
                        service_id = find['service_id']
                        dict = {
                            'service_id'  : service_id,
                            'service_name': find['service_name'],
                            'api_url'     : find['api_url'],
                            'permission'  : find['permission'],
                            'description' : find['description'],
                            'method'      : find['method'],
                            'param_set'   : find['param_set'],
                            'datetime'    : find['datetime']
                        }
                        jsonout[service_id] = dict 
            else:
                raise Exception('The status does not match the superuser', status)
            self.total['total'] = _services.count()
        except Exception as e:
            print(e, (type,(e)))
        return self.newService.SuperuserList(jsonout, self.total)
#=====================================================================================================#

    def ServiceAdd(self, data, jsonout):
        try:
            jsonout = {}
            dict(data)
            
            if _services.find({
                'service_name': data['service_name']
            }).count() > 0 or _services.find({
                'api_url': data['api_url']
            }).count() > 0 :
                msg = {
                    'message': 'Service name or Endpoint Already use',
                    'service_name': data['service_name']
                }
                
            
            else:
                epoch     = time.time()
                str_epoch = str(epoch)
                data['unix_time'] = str_epoch
                date_time = datetime.datetime.utcnow().replace(microsecond=0)+\
                    datetime.timedelta(hours=7)
                
                data['datetime'] = str(date_time)
                hash_lib = sha256(str_epoch.encode('utf-8')).hexdigest()
                data['service_id'] = hash_lib
    
                _services.insert_one(data)
                self.newLogs.ServiceLogs(data)          

                msg = {
                    'message'     : 'Create Success', 
                    'service_name': data['service_name'],
                    'api_url'     : data['api_url']
                }
            
        except Exception as e:
            print(e,(type,(e)))
            msg = {'message': 'Service name or EndPoint Already usee.'}
        jsonout = {'data': msg}
        return self.newService.ServiceAdd(jsonout)
#=====================================================================================================#

    def UserSignin(self, data, jsonout):
        try:
            jsonout = {}

            dict(data)
            for find in _users.find({'gg.gmail': data['gg']['gmail']}, {'gg.id_token': 0}):
                print ('ok')
                break
            else:
                epoch = time.time()
                data['unix_time'] = str(epoch)
                hash_lib = sha256(str(epoch).encode('utf-8')).hexdigest()
                data['user_id'] = hash_lib

                _users.insert_one(data)
                self.newLogs.UserLogs(data)

            for search in _users.find({'gg.gmail': data['gg']['gmail']}, {'gg.id_token': 0}):
                msg = {
                    'message'     : 'Login Success',
                    'user_id'     : search['user_id'],
                    'gmail'       : search['gg']['gmail'],
                    'google_photo': search['gg']['google_photo'],
                    'status'      : search['status']
                }
                break
        except Exception as e:
            print (e, (type, (e)))
            msg = 'Error Login'
        jsonout = {'data': msg}
        return self.newService.UserSignin(jsonout)
#=====================================================================================================#

    def UpdateService(self, data, jsonout):
        try:
            jsonout = {}
            for find in _services.find({'service_id': data['service_id']}):
                if (data['service_name'] and data['api_url'] and data['description'] and data['method'] 
                    and data['param_set'] ):
                    _services.update_one({
                        'service_id': data['service_id'], 'user_id': data['user_id']
                    },
                    {
                        '$set': {
                            'service_name': data['service_name'],
                            'api_url'     : data['api_url'],
                            'permission'  : data['permission'],
                            'description' : data['description'],
                            'method'      : data['method'],
                            'param_set'   : data['param_set']
                        }
                    })
                    data['datetime'] = str(datetime.datetime.utcnow().replace(microsecond=0)+\
                    datetime.timedelta(hours=7))
                    self.newLogs.UpdateLogs(data)
                    msg = {
                        'message'     : 'Update Success',
                        'service_name': data['service_name'],
                        'api_url'     : data['api_url'],
                        'permission'  : data['permission'],
                        'description' : data['description'],
                        'param_set'   : data['param_set'],
                        'datetime'    : data['datetime']
                    }
                    break
                else:
                    msg = {'msg': 'Data Not Found'}
            else:
                msg = {'msg': 'Service_id or User_id Not Found'}
                
        except Exception as e:
            print (e, (type, (e)))
            msg = 'Error'
        jsonout = {'data': msg}
        return self.newService.UpdateService(jsonout)
#=====================================================================================================#

    def SuperuserUpdate(self, data, jsonout):
        try:
            jsonout = {}

            if data['status'] == 'superuser':
                for find in _services.find({'service_id': data['service_id']}):
                    _services.update_one({
                        'service_id': data['service_id']
                    },
                    {
                        '$set':{
                            'service_name' : data['service_name'],
                            'api_url'      : data['api_url'],
                            'permission'   : data['permission'],
                            'description'  : data['description'],
                            'method'       : data['method'],
                            'param_set'    : data['param_set']
                        }
                    })

                    data['datetime'] = str(datetime.datetime.utcnow().replace(microsecond=0)+\
                        datetime.timedelta(hours=7))
                    self.newLogs.UpdateLogs(data)

                    msg = {
                        'message'     : 'Update Success',
                        'service_name': data['service_name'],
                        'api_url'     : data['api_url'],
                        'permission'  : data['permission'],
                        'description' : data['description'],
                        'param_set'   : data['param_set']
                    }

                    break
                else :
                    msg = {'message': 'Not Found'}
            else:
                 msg = {'message': 'The status does not match the superuser'}

        except Exception as e:
            print (e,(type,(e)))
            msg = 'Error'
        jsonout = {'data': msg}
        return self.newService.SuperuserUpdate(jsonout)
#=====================================================================================================#

    def DeleteService(self, data, jsonout):
        try:
            jsonout = {}

            for find in _services.find({'service_id': data['service_id'], 'user_id': data['user_id']}):
                _services.delete_one({'service_id': data['service_id'], 'user_id': data['user_id']})
                msg = {'message': 'Delete Success'}

                data['datetime'] = str(datetime.datetime.utcnow().replace(microsecond=0)+\
                    datetime.timedelta(hours=7))
                self.newLogs.DeleteLogs(data)
                break
        except Exception as e:
            print (e, (type,(e)))
            msg = {'message': 'Error'}
        jsonout = {'data': msg}
        return self.newService.DeleteService(jsonout)
#=====================================================================================================#

    def SuperuserDelete(self, servcie_id, status, jsonout):
        try:
            jsonout = {}
            
            if status == 'superuser':
                for find in _services.find({'service_id': servcie_id}):
                    _services.delete_one({'service_id': servcie_id})
                    msg = {'message': 'Delete Success'}
                    date_time = str(datetime.datetime.utcnow().replace(microsecond=0)+\
                        datetime.timedelta(hours=7))
                    self.newLogs.DeleteLogs(status, date_time)
                    break
                else:
                    msg = {'message': 'Not Found'}
            else:
                msg = {'message': 'The status does not match the superuser'}
        except Exception as e:
            print(e,(type,(e)))
            msg = {'message': 'Error'}
        jsonout = {'data': msg}
        return self.newService.SuperuserDelete(jsonout)
#=====================================================================================================#

    def Demo(self, data):
        try:
           

            param_name = []
            param_type = []
            desc       = []
            for find in data['param_set']:
                param_name.append(find['param_name'])
                param_type.append(find['param_type'])
                desc.append(find['desc'])
                print(param_name)
            dat = {
                'service_name': data['service_name'],
                'api_url' : data['api_url'],
                'permission': data['permission'],
                'user_id'  : data['user_id'],
                'description': data['description'],
                'method'    : data['method'],
                'param_name': param_name,
                'param_type': param_type,
                'desc'      : desc
            }
        except Exception as e:
            print(e, (type,(e)))
            dat = {'msg' : 'test'}
        # jsonout = {'dat': dat}
        return self.newService.Demo(dat)
#=====================================================================================================#

