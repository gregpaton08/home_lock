#!flask/bin/python

from DoorLockControllercontroller import DoorLockController
import time


def __debug_is_door_locked():
    lock = DoorLockController()
    current_state = lock.get()
    try:
        while True:
            if current_state != lock.get():
                current_state = lock.get()
                print("Door is {0}locked".format("" if current_state else "un"))
            else:
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass


def __debug_lock_door():
    lock = DoorLockController()
    print("Debug lock_door()")
    try:
        while True:
            input = raw_input("Enter 'L' for lock or 'U' for unlock: ")
            status = None
            if input is "l":
                status = True
            elif input is "u":
                status = False
            else:
                print("Invalid input {0}".format(input))
                continue

            if lock.set(status):
                print("Door is {0}locked".format("" if lock.get() else "un"))
            else:
                print("ERROR: failed to {0}lock door".format("" if status else "un"))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    __debug_is_door_locked()
    # __debug_lock_door()
