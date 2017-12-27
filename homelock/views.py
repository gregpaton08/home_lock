from flask import render_template, request
from homelock import app
from doorlock import DoorLock
from flask_restful import Resource, Api
import json

API_URL = '/api/v1/'

api = Api(app)

@app.route('/')
def hello_world():
    return render_template('index.html')


class LockAPI(Resource):
    def __init__(self):
        self.lock = DoorLock()

    def get(self):
        return { 'status' : self.lock.get() }

    def put(self):
        if not request.is_json:
            return { 'message' : 'Data provided must be in JSON format.' }, 400

        data = json.loads(request.data)
        self.lock.set(data['status'])
        return self.get()

api.add_resource(LockAPI, API_URL + 'lock_status')
