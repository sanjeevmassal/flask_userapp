class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments
    DEBUG = False
    SECRET_KEY = r'p9Bv<3Eid9%$i01p9Bv<3Eid9%$i0'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/flask_userapp'
    DEBUG = True
    SQLALCHEMY_ECHO = True
    TESTING = True


class ProductionConfig(Config):
    pass


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}