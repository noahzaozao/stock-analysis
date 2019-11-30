from urllib.parse import quote_plus


class Config:
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017
    MONGO_USERNAME = 'root'
    MONGO_PASSWORD = 'root.123'
    MONGO_DBNAME = 'stocks'
    MONGO_URI = 'mongodb://' + quote_plus(MONGO_USERNAME) + ':' + quote_plus(MONGO_PASSWORD) + '@' + MONGO_HOST + ':' + str(MONGO_PORT) + '/' + MONGO_DBNAME

    @staticmethod
    def init_app(app):
        pass


class AdminConfig:
    MONGO_HOST = Config.MONGO_HOST
    MONGO_PORT = Config.MONGO_PORT
    MONGO_USERNAME = 'root'
    MONGO_PASSWORD = 'root.123'
    MONGO_DBNAME = 'admin'
    MONGO_URI = 'mongodb://' + quote_plus(MONGO_USERNAME) + ':' + quote_plus(MONGO_PASSWORD) + '@' + MONGO_HOST + ':' + str(MONGO_PORT) + '/' + MONGO_DBNAME

    @staticmethod
    def init_app(app):
        pass


config = {
    'dev': Config,
}
