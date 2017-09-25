from flask import render_template, jsonify, request
from homelock import app
import lock_motor
from flask_restful import Resource, Api, reqparse

API_URL = '/api/v1/'

api = Api(app)

def string_to_boolean(input_string):
    if input_string.lower() == 'true':
        return True
    elif input_string.lower() == 'false':
        return False

    return None

@app.route('/')
def hello_world():
    return render_template('index.html')


class LockAPI(Resource):
    # def __init__(self):
    #     self.reqparse = reqparse.RequestParser()
    #     self.reqparse.add_argument('status', type = bool, required = True, help = 'Door lock status', location = 'json')
    #     super(LockAPI, self).__init__()

    def get(self):
        return { 'status' : lock_motor.is_door_locked() }

    def put(self):
        should_lock_door = string_to_boolean(request.form['status'])
        lock_motor.lock_door(should_lock_door)
        return { 'status' : lock_motor.is_door_locked() }

api.add_resource(LockAPI, API_URL + 'lock_status')
