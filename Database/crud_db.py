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
            i=0
            startat = (page - 1) * limit
            for find in _services.find({'permission': 'public'}).skip(startat).limit(limit):
                start = _users.find({'user_id' : find['user_id']})
                service_id = find['service_id']
                if find['param_set'] == [] :
    
                    dict = {
                        'ao'  : service_id,
                        'am'  : find['service_name'],
                        'wo'  : find['api_url'],
                        'od'  : find['permission'],
                        'sy'  : find['description'],
                        'ny'  : find['method'],
                        'oa'  : find['param_set'],
                        'fh'  : start[i]['gg']['gmail'],
                        'fy'  : find['datetime']
                    }
                    jsonout[service_id] = dict
                    
                else:
                    for state in find['param_set']:
                        state['om'] = state.pop('param_name')
                        state['oy'] = state.pop('param_type')
                        state['sv'] = state.pop('desc')

                    dict = {
                        'ao'  : service_id,
                        'am'  : find['service_name'],
                        'wo'  : find['api_url'],
                        'od'  : find['permission'],
                        'sy'  : find['description'],
                        'ny'  : find['method'],
                        'oa'  : find['param_set'],
                        'fh'  : start[i]['gg']['gmail'],
                        'fy'  : find['datetime']
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
            i=0
            startat = (page - 1) * limit
            for find in _services.find({'user_id': user_id}).skip(startat).limit(limit):
                start = _users.find({'user_id' : user_id})
                service_id = find['service_id']
                if find['param_set'] == [] :

                    dict = {
                        'ao'  : service_id,
                        'am'  : find['service_name'],
                        'wo'  : find['api_url'],
                        'od'  : find['permission'],
                        'sy'  : find['description'],
                        'ny'  : find['method'],
                        'oa'  : find['param_set'],
                        'fh'  : start[i]['gg']['gmail'],
                        'fy'  : find['datetime']
                    }
                    jsonout[service_id] = dict
                    
                else: 
                    for state in find['param_set']:
                        state['om'] = state.pop('param_name')
                        state['oy'] = state.pop('param_type')
                        state['sv'] = state.pop('desc')

                    dict = {
                        'ao'  : 'service_id',
                        'am'  : find['service_name'],
                        'wo'  : find['api_url'],
                        'od'  : find['permission'],
                        'sy'  : find['description'],
                        'ny'  : find['method'],
                        'oa'  : find['param_set'],
                        'fh'  : start[i]['gg']['gmail'],
                        'fy'  : find['datetime']
                    }
                    jsonout[service_id] = dict
                
                    
                
            self.total['total'] = _services.count({'user_id': user_id})
        except Exception as e:
            print(e, (type, (e)))

        return self.newService.MyApiList(jsonout, self.total)
#=====================================================================================================#

    def SuperuserList(self, page, limit, user_id, status, jsonout):
        try:
            jsonout = {}
            startat = (page - 1) * limit
            i=0
            state = _users.find({'user_id': user_id})
            assert state.count() != 0, 'Data not foud'
            assert state[0]['status'] == status, 'You not permission!!'
           
            for find in _services.find().skip(startat).limit(limit):
                start = _users.find({'user_id': find['user_id']})
                service_id = find['service_id']
                if find['param_set'] == [] :

                    dict = {
                        'ao'  : service_id,
                        'am'  : find['service_name'],
                        'wo'  : find['api_url'],
                        'od'  : find['permission'],
                        'sy'  : find['description'],
                        'ny'  : find['method'],
                        'oa'  : find['param_set'],
                        'fh'  : start[i]['gg']['gmail'],
                        'fy'  : find['datetime']
                    }
                    jsonout[service_id] = dict
                    
                else: 
                    for state in find['param_set']:
                        state['om'] = state.pop('param_name')
                        state['oy'] = state.pop('param_type')
                        state['sv'] = state.pop('desc')

                    dict = {
                        'ao'  : 'service_id',
                        'am'  : find['service_name'],
                        'wo'  : find['api_url'],
                        'od'  : find['permission'],
                        'sy'  : find['description'],
                        'ny'  : find['method'],
                        'oa'  : find['param_set'],
                        'fh'  : start[i]['gg']['gmail'],
                        'fy'  : find['datetime']
                    }
                    jsonout[service_id] = dict 
                
            self.total['total'] = _services.count()

        except AssertionError as e:
            print (e)
            jsonout['alert'] = str(e)
            return jsonout
    
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
                    'message': 'Create Success', 
                    'am'     : data['service_name'],
                    'wo'     : data['api_url']
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
            if _users.find({
                'gg.gmail': data['gg']['gmail']
            }).count() > 0:
                pass
            else:
                epoch = time.time()
                data['unix_time'] = str(epoch)
                hash_lib = sha256(str(epoch).encode('utf-8')).hexdigest()
                data['user_id'] = hash_lib

                _users.insert_one(data)
                self.newLogs.UserLogs(data)

            state = _users.find({'gg.gmail': data['gg']['gmail']})
            msg = {
                'message': 'Login Success',
                'yo'     : state[0]['user_id'],
                'ff'     : state[0]['gg']['gmail'],
                'fo'     : state[0]['gg']['google_photo'],
                'ar'     : state[0]['status']
            }

        except Exception as e:
            print (e, (type, (e)))
            msg = 'Error Login'
        jsonout = {'data': msg}
        return self.newService.UserSignin(jsonout)
#=====================================================================================================#

    def UpdateService(self, data, jsonout):
        try:
            jsonout = {}
            state = _services.find({'service_id': data['service_id']})
            assert state.count()       != 0, 'Service not found'
            assert state[0]['user_id'] == data['user_id'], 'ID not found'

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
                msg = {'message': 'Update Success'}

            else:
                msg = 'Update Failed'
        except AssertionError as e:
            msg = str(e)
        jsonout['alert'] = msg
        return self.newService.UpdateService(jsonout)
#=====================================================================================================#

    def SuperuserUpdate(self, data, jsonout):
        try:
            jsonout = {}
            state   = _users.find({'user_id': data['user_id']})
            assert state.count()      != 0, 'ID not found'
            assert state[0]['status'] == data['status'], 'You not permission'
            
            if (data['service_name'] and data['api_url'] and data['description'] and data['method'] 
                and data['param_set'] ): 
            
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
                msg = 'Update Success'
                data['datetime'] = str(datetime.datetime.utcnow().replace(microsecond=0)+\
                    datetime.timedelta(hours=7))
                self.newLogs.UpdateLogs(data)
            else:
                msg = 'Update Failed'
        except AssertionError as e:
            msg = str(e)

        jsonout['alert'] = msg
        return self.newService.SuperuserUpdate(jsonout)
#=====================================================================================================#

    def DeleteService(self, data, jsonout):
        try:
            jsonout = {}
            state   = _services.find({'service_id': data['service_id']})

            assert state.count()       != 0, 'Service not found'
            assert state[0]['user_id'] == data['user_id'], 'ID not found'

            _services.delete_one({'service_id': data['service_id'], 'user_id': data['user_id']})
            msg = 'Delete Success'

            data['datetime'] = str(datetime.datetime.utcnow().replace(microsecond=0)+\
                datetime.timedelta(hours=7))
            self.newLogs.DeleteLogs(data)
               
        except AssertionError as e:
            msg = str(e)
        jsonout['alert'] = msg
        return self.newService.DeleteService(jsonout)
#=====================================================================================================#

    def SuperuserDelete(self, service_id, user_id, status, jsonout):
        try:
            jsonout= {}
            state  = _users.find({'user_id': user_id})
            states = _services.find({'service_id': service_id})

            assert state.count()      != 0, 'Id not found'
            assert state[0]['status'] == status, 'You not permission'
            assert states.count()     != 0, 'Service not found'

            _services.delete_one({'service_id': service_id})
            msg = 'Delete Success'

        except AssertionError as e:
            msg = str(e)

        jsonout['alert'] = msg
        return self.newService.SuperuserDelete(jsonout)
#=====================================================================================================#
