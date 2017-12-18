#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

MOTOR_LOCK_PIN = 4 # Blue wire out of lock. Pin to set high to lock.
MOTOR_UNLOCK_PIN = 18 # Orange wire out of lock. Pin to set high to unlock.
MOTOR_SWITCH_PIN = 17 # Butterfly switch that signals when the lock is opened/closed.
LOCK_DIRECTION_CLOCKWISE = True # Set depending on the lock direction: True if a clockwise spin locks or FALSE if a counter-clockwise spin locks.

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTOR_LOCK_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_UNLOCK_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cleanup():
    GPIO.cleanup()

def is_door_locked():
    return LOCK_DIRECTION_CLOCKWISE != GPIO.input(MOTOR_SWITCH_PIN)

def lock_door(lock=True):
    if lock != is_door_locked():
        lock_pin = MOTOR_LOCK_PIN if lock else MOTOR_UNLOCK_PIN
        end_time = time.time() + 2 # seconds
        # Run loop until the timeout is hit or until door is at desired state, whichever comes first.
        GPIO.output(lock_pin, GPIO.HIGH)
        time_out = False
        while lock != is_door_locked() and not time_out:
            time.sleep(0.1)
            if time.time() > end_time:
                time_out = True

        # Sleep momentarily to allow the lock to fully turn.
        if not time_out:
            time.sleep(0.5)

        GPIO.output(lock_pin, GPIO.LOW)

    return lock == is_door_locked()

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
            else:
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass#cleanup()

def __debug_lock_door():
    print('Debug lock_door()')
    try:
        while True:
            input = raw_input('Enter \'L\' for lock or \'U\' for unlock: ')
            status = None
            if input is 'l':
                status = True
            elif input is 'u':
                status = False
            else:
                print('Invalid input {0}'.format(input))
                continue

            if lock_door(status):
                print('Door is {0}locked'.format('' if is_door_locked() else 'un'))
            else:
                print('ERROR: failed to {0}lock door'.format('' if status else 'un'))
    except KeyboardInterrupt:
        cleanup()

if __name__ == '__main__':
    setup()
    # __debug_is_door_locked()
    __debug_lock_door()
