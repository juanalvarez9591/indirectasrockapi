import os
from flask import Flask, render_template
import json
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/indirecta', methods=['GET'])
def get():
    f = open("indirectas.json")
    x = json.load(f)
    length = len(x)-1

    randindex = random.randint(0, length)

    return(str(x[randindex][0]))


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
