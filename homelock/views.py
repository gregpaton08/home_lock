from flask import render_template, jsonify, request
from homelock import app
from doorlock import doorlock
from flask_restful import Resource, Api, reqparse
import json

API_URL = '/api/v1/'

api = Api(app)

@app.route('/')
def hello_world():
    return render_template('index.html')


class LockAPI(Resource):
    # def __init__(self):
    #     self.reqparse = reqparse.RequestParser()
    #     self.reqparse.add_argument('status', type = bool, required = True, help = 'Door lock status', location = 'json')
    #     super(LockAPI, self).__init__()

    def get(self):
        return { 'status' : doorlock.is_door_locked() }

    def put(self):
        if not request.is_json:
            return { 'message' : 'Data provided must be in JSON format.' }, 400

        data = json.loads(request.data)
        doorlock.lock_door(data['status'])
        return self.get()

api.add_resource(LockAPI, API_URL + 'lock_status')
