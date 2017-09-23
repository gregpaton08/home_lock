from flask import render_template, jsonify, request
from homelock import app
import lock_motor

def string_to_boolean(input_string):
    if input_string.lower() == 'true':
        return True
    elif input_string.lower() == 'false':
        return False

    return None

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/lock_status')
def lock_status():
    return jsonify(locked=lock_motor.is_door_locked())

@app.route('/lock')
def lock():
    should_lock_door = request.args.get('lock', None)
    if should_lock_door is not None:
        lock_motor.lock_door(string_to_boolean(should_lock_door))

    return render_template('index.html')