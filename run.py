from homelock import app, doorlock
import sys

if __name__ == '__main__':
    doorlock.doorlock.setup()
    try:
        app.run(host='0.0.0.0', port=sys.argv[1])
    finally:
        doorlock.doorlock.cleanup()