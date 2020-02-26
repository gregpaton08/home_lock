# Home Lock

Wifi + BLE connected deadbolt powered by a Raspberry Pi

## Deployment

### Prerequisites

Install the prerequisite packages.

```bash
sudo sudo apt-get install -y python3-pip
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
```

Add the script to `cron` to start up on boot.

```bash
sudo crontab -
# add the following line
# @reboot nohup /home/pi/home_lock/run.sh &
```

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

## Misc.

### Accessing the virtualenv

```bash
# enter
source env/bin/activate
# exit
deactivate
```
