from flask import render_template, request
from .homelock import app
from .doorlockcontroller import DoorLockController
from flask_restful import Resource, Api
import json

API_URL = '/api/v1/'

api = Api(app)

door_lock_controller = DoorLockController()

@app.route('/')
def index():
    return render_template('index.html')


class LockAPI(Resource):
    def __init__(self):
        pass

    def __repr__(self):
        return "%s()" % (self.__class__)

    def get(self):
        return { 'status' : door_lock_controller.get() }

    def put(self):
        if not request.is_json:
            return { 'message' : 'Data provided must be in JSON format.' }, 400

        data = json.loads(request.data)
        door_lock_controller.set(data['status'])
        return self.get()

api.add_resource(LockAPI, API_URL + 'lock_status')
