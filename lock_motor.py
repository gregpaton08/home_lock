#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

MOTOR_LOCK_PIN = 4
MOTOR_UNLOCK_PIN = 18 # still need to solder and hook this up.
MOTOR_SWITCH_PIN = 17 # Butterfly switch that signals when the lock is opened/closed.

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTOR_LOCK_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_UNLOCK_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cleanup():
    GPIO.cleanup()

def is_door_locked():
    return GPIO.input(MOTOR_SWITCH_PIN)

def lock_door(lock=True):
    if lock != is_door_locked():
        lock_pin = MOTOR_LOCK_PIN if lock else MOTOR_UNLOCK_PIN
        time_out = 1 # seconds
        end_time = time.time() + time_out
        # Run loop for time_out seconds or until door is at desired state, whichever comes first.
        GPIO.output(lock_pin, GPIO.HIGH)
        while lock != is_door_locked() and time.time() < end_time:
            time.sleep(0.1)
        GPIO.output(lock_pin, GPIO.LOW)

def __debug_is_door_locked():
    current_state = is_door_locked()
    try:
        while True:
            if current_state != is_door_locked():
                current_state = is_door_locked()
                if current_state:
                    print('Door Locked')
                else:
                    print('Door unlocked')
    except KeyboardInterrupt:
        cleanup()

def __debug_lock_door():
    print('Debug lock_door()')
    try:
        while True:
            input = raw_input('Enter \'L\' for lock or \'U\' for unlock: ')
            if input is 'l':
                lock_door(True)
            elif input is 'u':
                lock_door(False)
            else:
                print('Invalid input {0}'.format(input))
            print('Door is {0}locked'.format('' if is_door_locked() else 'un'))
    except KeyboardInterrupt:
        cleanup()

if __name__ == '__main__':
    setup()
    # __debug_is_door_locked()
    __debug_lock_door()
