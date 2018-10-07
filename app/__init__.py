from flask import Flask
from flask_user import UserManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from app.extensions import db, login_manager, mail, admin_panel
from .conf import app_conf, blueprints


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
    app.config.from_object(app_conf[config_name])
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'accounts:login'
    mail.init_app(app)
    migrate = Migrate(app, db)
    toolbar = DebugToolbarExtension(app)
    from accounts import models as account_models
    UserManager(app, db, account_models.User)
    init_admin(app,db)
    init_blueprints(app)
    app.debug = True
    return app


def init_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def init_admin(app, db):
    admin_panel.init_app(app)
