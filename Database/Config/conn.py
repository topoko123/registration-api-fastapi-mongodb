from Database.Config.db_config import mongodb_url, port, MongoClient
client = MongoClient(mongodb_url, port)
db = client['api_url']