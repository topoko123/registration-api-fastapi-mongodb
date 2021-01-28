from pymongo import MongoClient
import Database.Config.db_config as settings
#=====================================================================================================#

client = MongoClient(settings.mongodb_url, settings.port)
db = client['api_db']
#=====================================================================================================#
