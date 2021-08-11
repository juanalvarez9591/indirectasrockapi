import json
import random
import os
from flask import Flask
from flask.helpers import send_from_directory
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class IndirectaRock(Resource):
    def get(self):
        f = open("indirectas.json")
        x = json.load(f)
        length = len(x)-1

        randindex = random.randint(0, length)

        return(str(x[randindex][0]))


api.add_resource(IndirectaRock, '/')

if __name__ == '__main__':
    app.run()
