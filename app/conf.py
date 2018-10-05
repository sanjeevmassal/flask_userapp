from .views import home as home_blueprint
from accounts import account as account_blueprint
from admin import admin as admin_blueprint
from carapp import carapp as carapp_blueprint


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = r'y9&3t1nzm)+0^9d=hc_ev(u3r!m-4ij=32a4s-=4rk95$57#-%'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(BaseConfig):
    DEBUG = True
    SECRET_KEY = r'y9&3t1nzm)+0^9d=h3edfrc_ev(u3r!m-4ij=32a4s-=4rk95$57#-%'
    SQLALCHEMY_DATABASE_URI = r'mysql://root:root@localhost/flask_userapp'
    PORT = 8080
    MAIL_SERVER = r'smtp.mailtrap.io'
    MAIL_USERNAME = r'4c882d203d04f1'
    MAIL_PASSWORD = r'8e00561cb6cbb8'
    MAIL_DEFAULT_SENDER = r'abc@gmail.com'
    USER_EMAIL_SENDER_EMAIL = r'abc@gmail.com'
    MAIL_PORT = 2525

class Production(BaseConfig):
    SECRET_KEY = r'y9&3t1nzm)+0^9d=h3ssedfrc_ev(u3r!m-4ij=32a4s-=4rk95$57#-%'
    SQLALCHEMY_DATABASE_URI = r"postgresql://postgres@localhost/ms_hdfc_life"
    PORT = 9090

app_conf = {
    'development' : Development,
    'production' : Production
}

blueprints = {
    home_blueprint,
    account_blueprint,
    carapp_blueprint,
    admin_blueprint
}