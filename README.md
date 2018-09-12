# Home Lock

Wifi + BLE connected deadbolt powered by a Raspberry Pi

## Interacting with the API

### CURL

```
# Getting the lock status
curl http://<RPi address>:<RPi port>/api/v1/lock_status -X GET

# Lock
curl http://<RPi address>:<RPi port>/api/v1/lock_status -X PUT -H "Content-Type: application/json" -d "{\"status\":true}"

# Unlock
curl http://<RPi address>:<RPi port>/api/v1/lock_status -X PUT -H "Content-Type: application/json" -d "{\"status\":false}"
```

## Wifi Issues

If wifi connection cuts out intermittently then do the following:

1. Create and edit a conf file  
```
sudo nano /etc/modprobe.d/8192cu.conf
```

2. Write the following, save, and exit.
```
# Disable power management
options 8192cu rtw_power_mgnt=0 rtw_enusbss=0
```

3. Reboot  
```
sudo reboot
```