HOST = 'localhost'
PORT = 3306
DB_NAME = 'auto_ds'
USER = 'root'
PASSWORD = 'root'

SQLALCHEMY_DATABASE_URI = f'mysql+aiomysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
