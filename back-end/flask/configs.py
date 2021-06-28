HOST = 'localhost'
PORT = '3306'
DATABASE = 'bsdb'
USERNAME = 'root'
PASSWORD = '1'

DB_URI = "mysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False

JSON_AS_ASCII = False