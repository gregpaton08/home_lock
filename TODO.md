# To Do

## Tasks
* improve and test lock logic - UNIT TESTS!
    * test javascript is working with API
    * setup so tests can be run on any machine (not hardware dependent) (may require mock objects)
* switch over to RPi zero
* install RPi zero inside enclosure
* add support for BLE
    * public/private key encryption for BLE?
* log history of lock/unlock (use database)
* push notifications to iPhone when door locked/unlocked

## Completed Tasks
* implement restful API
* solder wires to motor pins (annotated in notes image)
* disconnect butterfly switch from circuit board and connect to RPi
* tie butterfly switch circuit board connection to ground
* setup webserver (flask?)

## Stretch goals
* sms integration - text code to number to unlock door allowing temporary entry to visitors
* email integration - same as above, but via email (security is a concern for both)
* push notification for iOS - get notified whenever door is locked/unlocked
* run on heroku, control from anywhere (security, security, security)
