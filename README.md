# Home Lock

Wifi + BLE connected deadbolt powered by a Raspberry Pi

## Interacting with the API

## CURL

```
# Getting the lock status
curl http://<RPi address>:<RPi port>/api/v1/lock_status -X GET

# Lock
curl http://<RPi address>:<RPi port>/api/v1/lock_status -X PUT -d "status=true"

# Unlock
curl http://<RPi address>:<RPi port>/api/v1/lock_status -X PUT -d "status=false"
```
