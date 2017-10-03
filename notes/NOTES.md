# Notes

## References

[PT4303](http://www.dzsc.com/uploadfile/company/307703/201246135150265.pdf)  
[PIC16LF1829](http://ww1.microchip.com/downloads/en/DeviceDoc/41440B.pdf)  
[C3021LD](https://www.diodes.com/assets/Datasheets/ds32152.pdf)  
[H-Bridge](http://www.modularcircuits.com/blog/articles/h-bridge-secrets/h-bridges-the-basics/)  
[RPi Push Switch](http://razzpisampler.oreilly.com/ch07.html)  
[RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)  
[RPi Bluetooth](https://www.raspberrypi.org/forums/viewtopic.php?p=947185#p947185)  
[RPi POE](https://raspberrypi.stackexchange.com/questions/715/how-do-i-modify-my-raspberry-pi-to-be-powered-over-poe)  

### Notes

#### BLE

[iOS BLE](https://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/PerformingCommonCentralRoleTasks/PerformingCommonCentralRoleTasks.html#//apple_ref/doc/uid/TP40013257-CH3-SW1)  
[RPi Bluetooth discoverable](https://stackoverflow.com/questions/37927606/how-do-i-make-raspberry-pi-3-discoverable-for-ios-and-corebluetooth)  
[RPi BLE thread](https://www.raspberrypi.org/forums/viewtopic.php?t=78838)  
[RPi BLE thread](https://www.raspberrypi.org/forums/viewtopic.php?p=521067#p521067)  
[L2CAP Socket](https://stackoverflow.com/questions/20682294/bluez-advertise-service-gatt-server-example)  
[bleno](https://github.com/sandeepmistry/bleno/blob/master/examples/echo/characteristic.js)  
[bleno tutorial](http://www.raspberry-pi-geek.com/Archive/2014/08/Getting-BLE-to-behave-on-the-Pi/(offset)/2)  

```
# Enable BLE broadcast.
sudo hciconfig hci0 leadv 0

# Advertise BLE service.
sudo hcitool -i hci0 cmd 0x08 0x0008 15 02 01 1a 11 07 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50 00 00 00 00 00 00 00 00 00 00
```