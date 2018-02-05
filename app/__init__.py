from flask import Flask
from .config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)

    return app
