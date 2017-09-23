from homelock import app
import sys
import lock_motor

if __name__ == '__main__':
    lock_motor.setup()
    try:
        app.run(host='0.0.0.0', port=sys.argv[1])
    finally:
        lock_motor.cleanup()