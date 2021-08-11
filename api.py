import json
import random
from flask import Flask
from flask.helpers import send_from_directory
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        f = open("indirectas.json")
        x = json.load(f)
        length = len(x)-1

        randindex = random.randint(0, length)

        return(x[randindex][0])


api.add_resource(HelloWorld, '/')
