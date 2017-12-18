#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

class DoorLock:
    def __init__(self):
        self.__motor_lock_pin = 4 # Blue wire out of lock. Pin to set high to lock.
        self.__motor_unlock_pin = 18 # Orange wire out of lock. Pin to set high to unlock.
        self.__motor_switch_pin = 17 # Butterfly switch that signals when the lock is opened/closed.
        self.__lock_direction_clockwise = True # Set depending on the lock direction: True if a clockwise spin locks or FALSE if a counter-clockwise spin locks.

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__motor_lock_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.__motor_unlock_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.__motor_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def cleanup():
        GPIO.cleanup()

    def set(self, status):
        if status != self.get():
            lock_pin = self.__motor_lock_pin if status else self.__motor_unlock_pin
            end_time = time.time() + 2 # seconds
            # Run loop until the timeout is hit or until door is at desired state, whichever comes first.
            GPIO.output(lock_pin, GPIO.HIGH)
            time_out = False
            while status != self.get() and not time_out:
                time.sleep(0.1)
                if time.time() > end_time:
                    time_out = True

            # Sleep momentarily to allow the lock to fully turn.
            if not time_out:
                time.sleep(0.5)

            GPIO.output(lock_pin, GPIO.LOW)

        return status == self.get()

    def get(self):
        return self.__lock_direction_clockwise != GPIO.input(self.__motor_switch_pin)


def __debug_is_door_locked():
    lock = DoorLock()
    current_state = lock.get()
    try:
        while True:
            if current_state != lock.get():
                current_state = lock.get()
                print('Door is {0}locked'.format('' if current_state else 'un'))
            else:
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass

def __debug_lock_door():
    lock = DoorLock()
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

            if lock.set(status):
                print('Door is {0}locked'.format('' if lock.get() else 'un'))
            else:
                print('ERROR: failed to {0}lock door'.format('' if status else 'un'))
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    # __debug_is_door_locked()
    __debug_lock_door()
