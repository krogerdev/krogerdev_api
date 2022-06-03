# If you're seeing this and it's not working. It needs a config.py file with configs

# Required imports
from flask import Flask
from flask_restful import Api
import configparser

# Local imports
from content import Public, Notfound


def createapp():
    config = configparser.ConfigParser()
    config.read('config.ini')

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Public, '/<string:crumb>', resource_class_kwargs={'content': "test"})

    return app
