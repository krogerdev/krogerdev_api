from flask_restful import Resource


class Notfound(Resource):
    def __init__(self):
        pass

    def get(self):
        return {
            "data": "404 not found"
        }