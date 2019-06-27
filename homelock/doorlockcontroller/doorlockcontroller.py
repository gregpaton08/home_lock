import RPi.GPIO as GPIO
import time
import datetime
import sys


class DoorLockController:
    def __init__(self):
        GPIO.cleanup()
        self.__motor_lock_pin = 4 # Blue wire out of lock. Pin to set high to lock.
        self.__motor_unlock_pin = 18 # Orange wire out of lock. Pin to set high to unlock.
        self.__motor_switch_pin = 27 # Limit switch that signals when the lock is opened/closed.
        self.__lock_direction_clockwise = True # Set depending on the lock direction: True if a clockwise spin locks or FALSE if a counter-clockwise spin locks.

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__motor_lock_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.__motor_unlock_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.__motor_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        GPIO.add_event_detect(self.__motor_switch_pin, GPIO.BOTH, callback=self.status_change_callback)

        self.last_event_time = 0

    
    def __repr__(self):
        return "%s()" % (self.__class__)

    def cleanup():
        GPIO.cleanup()

    def status_change_callback(self, channel):
	# Debounce the switch.
	current_time = time.time()
	if current_time - self.last_event_time > 0.25:
		self.last_event_time = current_time
		print(str(datetime.datetime.now()) + ': Door ' + ('locked' if self.get() else 'unlocked'))
		sys.stdout.flush()

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
                time.sleep(0.25)

            GPIO.output(lock_pin, GPIO.LOW)

        return status == self.get()

    # Get the status of the door lock. Returns True if locked or False if unlocked.
    def get(self):
        return self.__lock_direction_clockwise != GPIO.input(self.__motor_switch_pin)
