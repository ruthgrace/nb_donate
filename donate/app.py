import os
from flask import Flask
from donate.extensions import db, migrate
from donate.settings import ProdConfig
from donate.models import (
    User,
    Account,
    Project,
    Currency,
    Transaction,
)


def create_app(config_object=ProdConfig):

    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)

    register_extensions(app)
    register_shellcontext(app)

    return(app)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_shellcontext(app):
    def shell_context():
        return{
            'db': db,
            'user': User,
            'account': Account,
            'project': Project,
            'ccy': Currency,
            'tx': Transaction
        }

    app.shell_context_processor(shell_context)