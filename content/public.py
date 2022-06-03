from flask_restful import Resource


class Public(Resource):
    content = ""

    def __init__(self, content):
        self.content = content

    def get(self, crumb):
        return {
            "data": crumb
        }