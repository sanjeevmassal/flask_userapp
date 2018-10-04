from .views import home as home_blueprint
from accounts import account as account_blueprint
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'y9&3t1nzm)+0^9d=hc_ev(u3r!m-4ij=32a4s-=4rk95$57#-%'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEFAULT_NLP_ENGINE = "witai"

class Development(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'y9&3t1nzm)+0^9d=h3edfrc_ev(u3r!m-4ij=32a4s-=4rk95$57#-%'
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/flask_userapp'
    PORT = 8080

class Production(BaseConfig):
    SECRET_KEY = 'y9&3t1nzm)+0^9d=h3ssedfrc_ev(u3r!m-4ij=32a4s-=4rk95$57#-%'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres@localhost/ms_hdfc_life"
    DEFAULT_NLP_ENGINE = "apiai"
    PORT = 9090

app_conf = {
    'development' : Development,
    'production' : Production
}

blueprints = {
    home_blueprint,
    account_blueprint
}