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
    lock_pin = MOTOR_LOCK_PIN if lock else MOTOR_UNLOCK_PIN
    end_time = time.time() + 4
    # Run loop for 4 seconds or until door is at desired state, whichever comes first.
    while lock != is_door_locked() and time.time() < end_time:
        GPIO.output(lock_pin, GPIO.HIGH)
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
    pass

if __name__ == '__main__':
    setup()
    __debug_is_door_locked()
