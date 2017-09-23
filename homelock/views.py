from flask import render_template, jsonify, request
from homelock import app
import lock_motor

@app.route('/')
def hello_world():
    return 'Hello, world!!!'

@app.route('/lock_status')
def lock_status():
    return jsonify(locked=lock_motor.is_door_locked())

@app.route('/lock')
def lock():
    print(request.args)
    return 'hello_world'