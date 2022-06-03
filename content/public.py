from flask_restful import Resource


class Public(Resource):
    def __init__(self):
        pass

    def get(self):
        return {
            "data": "Hello World!"
        }