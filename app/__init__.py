# Required imports
from flask import Flask
from flask_restful import Api

# Local imports
from content import Public

def createapp():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Public, '/')

    return app
