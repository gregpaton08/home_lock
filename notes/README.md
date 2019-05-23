# Notes

## REST API

curl http://192.168.1.168:5555/api/v1/lock_status -X PUT -H "Content-Type: application/json" -d "{\"status\":true}"

curl http://192.168.1.168:5555/api/v1/lock_status -X PUT -H "Content-Type: application/json" -d "{\"status\":false}"

## References

[PT4303](http://www.dzsc.com/uploadfile/company/307703/201246135150265.pdf)  
[PIC16LF1829](http://ww1.microchip.com/downloads/en/DeviceDoc/41440B.pdf)  
[C3021LD](https://www.diodes.com/assets/Datasheets/ds32152.pdf)  
[H-Bridge](http://www.modularcircuits.com/blog/articles/h-bridge-secrets/h-bridges-the-basics/)  
[RPi Push Switch](http://razzpisampler.oreilly.com/ch07.html)  
[RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)  
[RPi Bluetooth](https://www.raspberrypi.org/forums/viewtopic.php?p=947185#p947185)  
[RPi POE](https://raspberrypi.stackexchange.com/questions/715/how-do-i-modify-my-raspberry-pi-to-be-powered-over-poe)  

## BLE

[iOS BLE](https://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/PerformingCommonCentralRoleTasks/PerformingCommonCentralRoleTasks.html#//apple_ref/doc/uid/TP40013257-CH3-SW1)  
[RPi Bluetooth discoverable](https://stackoverflow.com/questions/37927606/how-do-i-make-raspberry-pi-3-discoverable-for-ios-and-corebluetooth)  
[RPi BLE thread](https://www.raspberrypi.org/forums/viewtopic.php?t=78838)  
[RPi BLE thread](https://www.raspberrypi.org/forums/viewtopic.php?p=521067#p521067)  
[L2CAP Socket](https://stackoverflow.com/questions/20682294/bluez-advertise-service-gatt-server-example)  
[bleno](https://github.com/sandeepmistry/bleno/blob/master/examples/echo/characteristic.js)  
[bleno tutorial](http://www.raspberry-pi-geek.com/Archive/2014/08/Getting-BLE-to-behave-on-the-Pi/(offset)/2)  

~~Setup RPi as iBeacon? iPhone will detect and awake, send signal to lock to open it?~~  
^ Use iPhones location change to run app in background

```
# Enable BLE broadcast.
sudo hciconfig hci0 leadv 0

# Advertise BLE service.
sudo hcitool -i hci0 cmd 0x08 0x0008 15 02 01 1a 11 07 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50 00 00 00 00 00 00 00 00 00 00
```

## Motor

The model of the motor is [FC-280SA-2865](https://product.mabuchi-motor.com/detail.html?id=48). According to the data sheet the current draw can go up to 5A (!) during a stall, which is well over the ~200ma output of the Raspberry Pi 5V pin. May want to find a way to limit this current draw. Also will want to power it separately from the RPi, instead of off of the 5V pin.
