# from typing import Dict, Optional, Tuple
from typing import Dict, Tuple, Optional
from Database.logs_db import Logs
from app.Service import Service
from hashlib import sha256
import Database.Config.conn as connect
import time
import datetime
from app.staterole import UserRole as user_role
import pymongo
#=====================================================================================================#

_services      = connect.db.service
_users         = connect.db.user

#=====================================================================================================#

class DB:
    newLogs    = Logs()
    newService = Service()
    total      = {}
#=====================================================================================================#

    def ApiList(self, page: int, limit: int, filter: int, jsonout: Dict) -> Tuple[str, int]: 
        try:        
            jsonout = {}
            i=0
            startat = (page - 1) * limit
            for find in _services.find({'permission': 'public'}).sort([("datetime", filter)]).skip(startat).limit(limit):
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

    def MyApiList(self, page: int, limit: int, user_id: str, filter: int, jsonout: Dict) -> Tuple[str, int]:
        try:
            jsonout = {}
            i=0
            startat = (page - 1) * limit
            for find in _services.find({'user_id': user_id}).sort([("datetime", filter)]).skip(startat).limit(limit):
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
                
                    
                
            self.total['total'] = _services.count({'user_id': user_id})
        except Exception as e:
            print(e, (type, (e)))

        return self.newService.MyApiList(jsonout, self.total)
#=====================================================================================================#

    def SuperuserList(self, page: int, limit: int, user_id: str, status: str, filter: int, jsonout: Dict) -> Tuple[str, int] :
        try:
            jsonout = {}
            startat = (page - 1) * limit
            i=0

            user_role.SuperuserList(user_id, status)           

            for find in _services.find().sort([("datetime", filter)]).skip(startat).limit(limit):
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
                
            self.total['total'] = _services.count()

        except AssertionError as e:
            print (e)
            jsonout['alert'] = str(e)
            return jsonout
    
        return self.newService.SuperuserList(jsonout, self.total)
#=====================================================================================================#

    def ServiceAdd(self, data: Dict, jsonout: Dict) -> Dict[str, str] :
        try:
            jsonout = {}
            dict(data)
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

        except pymongo.errors.DuplicateKeyError as e:
            msg = 'Servicename or EndPoint is Already in use.'
            
        jsonout = {'data': msg}
        return self.newService.ServiceAdd(jsonout)
#=====================================================================================================#

    def UserSignin(self, data: Dict, jsonout: Dict) -> Dict[str, str]:
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

                date_time = datetime.datetime.utcnow().replace(microsecond=0)+\
                datetime.timedelta(hours=7)
                data['datetime'] = str(date_time)

                data['user_id'] = hash_lib
            
                _users.insert_one(data)
                self.newLogs.UserLogs(data)

            state = _users.find({'gg.gmail': data['gg']['gmail']})
            if state[0]['ll'] is None:
                pass

            msg = {
                'message': 'Login Success',
                'alert'  : 'll_exists',
                'yo'     : state[0]['user_id'],
                'ff'     : state[0]['gg']['gmail'],
                'fo'     : state[0]['gg']['google_photo'],
                'ar'     : state[0]['status']
            }
        except KeyError as e:
            msg = {
                'message': 'Login Success',
                'alert'  : 'll_not_exists',
                'yo'     : state[0]['user_id'],
                'ff'     : state[0]['gg']['gmail'],
                'fo'     : state[0]['gg']['google_photo'],
                'ar'     : state[0]['status']
            }

        jsonout = {'data': msg}
        return self.newService.UserSignin(jsonout)

#=====================================================================================================#

    def LineSignin(self, data: Dict, jsonout: Dict) -> Dict[str, str]:
        try:
            jsonout = {}
            if _users.find({
                'll.ul_id': data['ll']['ul_id']
            }).count() > 0:
                pass
            else:
                epoch = time.time()
                data['unix_time'] = str(epoch)
                hash_lib = sha256(str(epoch).encode('utf-8')).hexdigest()
                
                date_time = datetime.datetime.utcnow().replace(microsecond=0)+\
                datetime.timedelta(hours=7)
                data['datetime'] = str(date_time)

                data['user_id'] = hash_lib
            
                _users.insert_one(data)
                self.newLogs.UserLogs(data)

            state = _users.find({'ll.ul_id': data['ll']['ul_id']})
            if state[0]['gg'] is None:
                pass

            msg = {
                'message': 'Login Success',
                'alert'  : 'gg_exists',
                'yo'     : state[0]['user_id'],
                'sb'     : state[0]['ll']['displayname'],
                'or'     : state[0]['ll']['picture'],
                'ar'     : state[0]['status']
            }
        except KeyError as e:
            msg = {
                'message': 'Login Success',
                'alert'  : 'gg_not_exists',
                'yo'     : state[0]['user_id'],
                'sb'     : state[0]['ll']['displayname'],
                'or'     : state[0]['ll']['picture'],
                'ar'     : state[0]['status']
            }

        jsonout = {'data': msg}
        return self.newService.LineSignin(jsonout)
#=====================================================================================================#

    def UpdateService(self, data: Optional[Dict], jsonout: Dict) -> Dict[str, str] :
        try:
            jsonout = {}
            user_role.MyserviceUpdate(data)

            if (data['service_name'] and data['api_url'] and data['description'] and data['method']):
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
        except pymongo.errors.DuplicateKeyError as e:
            msg = 'Servicename or EndPoint is Already in use.'

        jsonout['alert'] = msg
        return self.newService.UpdateService(jsonout)
#=====================================================================================================#

    def SuperuserUpdate(self, data: Optional[Dict], jsonout: Dict) -> Dict[str, str] :
        try:
            jsonout = {}
            user_role.SuperuserUpdate(data)
            
            if (data['service_name'] and data['api_url'] and data['description'] and data['method']): 
            
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
        except pymongo.errors.DuplicateKeyError as e:
            msg = 'Servicename or EndPoint is Already in use.'

        jsonout['alert'] = msg
        return self.newService.SuperuserUpdate(jsonout)
#=====================================================================================================#

    def GG_add_Line(self, data: Optional[Dict], jsonout: Dict) -> Dict[str, str]:
        try:
            jsonout = {}
            if (data['access_token'] and data['displayname'] and data['ul_id'] and data['id_li_tk']):

                _users.update_one({
                    'user_id': data['user_id']
                },
                {
                    '$set': {
                        'll.access_token': data['access_token'],
                        'll.displayname' : data['displayname'],
                        'll.ul_id' : data['ul_id'],
                        'll.picture' : data['picture'],
                        'll.id_li_tk' : data['id_li_tk']
                    }
                })
                msg = 'll_exists'
        except Exception as e:
            print (e ,(type, (e)))
        jsonout['alert'] = msg
        return self.newService.GG_add_Line(jsonout)
#=====================================================================================================#

    def LL_add_gg(self, data: Optional[Dict], jsonout: Dict) -> Dict[str, str]:
        try:
            jsonout = {}
            if (data['id_token'] and data['fullname'] and data['gmail']):

                _users.update_one({
                    'user_id': data['user_id'],
                },
                {
                    '$set': {
                        'gg.id_token' : data['id_token'],
                        'gg.fullname' : data['fullname'],
                        'gg.gmail'    : data['gmail'],
                        'gg.google_photo' : data['google_photo']
                    }
                })
                msg = 'gg_exists'
        except Exception as e:
            print (e, (type,(e)))
        jsonout['alert'] = msg
        return self.newService.LL_add_gg(jsonout)
#=====================================================================================================#


    def DeleteService(self, data: Dict, jsonout: Dict) -> Dict[str, str] :
        try:
            user_role.MyserviceDel(data)

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

    def SuperuserDelete(self, data: Dict, jsonout: Dict) -> Dict[str, str]:
        try:
            jsonout= {}
            user_role.SuperuserDel(data)
            _services.delete_one({'service_id': data['service_id']})
            msg = 'Delete Success'

        except AssertionError as e:
            msg = str(e)

        jsonout['alert'] = msg
        return self.newService.SuperuserDelete(jsonout)
#=====================================================================================================#
