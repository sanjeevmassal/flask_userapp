import jinja2
from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from app.extensions import db, login_manager
from .conf import app_conf, blueprints


class UserApp(Flask):
    def __init__(self, *args, **kwargs):
        Flask.__init__(self, *args, **kwargs)
        self.jinja_loader = jinja2.ChoiceLoader([
            self.jinja_loader,
            jinja2.PrefixLoader({}, delimiter=".")
        ])

    def create_global_jinja_loader(self):
        return self.jinja_loader

    def register_blueprint(self, bp, *args, **kwargs):
        Flask.register_blueprint(self, bp, *args, **kwargs)
        self.jinja_loader.loaders[1].mapping[bp.name] = bp.jinja_loader


def create_app(config_name):
    app = UserApp(__name__, instance_relative_config=True)
    Bootstrap(app)
    app.config.from_object(app_conf[config_name])
    db.init_app(app)
    migrate = Migrate(app, db)
    toolbar = DebugToolbarExtension(app)
    from accounts import models
    login_manager.init_app(app)
    init_blueprints(app)
    app.debug = True
    return app


def init_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
