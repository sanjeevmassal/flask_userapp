import os
from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from app.extensions import db, login_manager
from .conf import app_conf

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=['GET', 'POST'])
    def home():
        return 'here'

    Bootstrap(app)
    app.config.from_object(app_conf[config_name])
    #app.config.from_pyfile('conf.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    from accounts import models
    login_manager.init_app(app)
    return app
