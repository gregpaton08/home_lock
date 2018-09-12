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
* research: does August Lock wifi hub require port forwarding?
  * [Reverse engineering the Nest](http://experimental-platform.tumblr.com/post/137835649425/reverse-engineering-google-nest-devices)
  * websockets? see [this](https://www.raspberrypi.org/forums/viewtopic.php?t=115936)
  * [REST streaming](https://developers.nest.com/documentation/cloud/rest-streaming-guide)
  * [WebSockets](https://www.pubnub.com/blog/2015-01-05-websockets-vs-rest-api-understanding-the-difference/)
  * [socket.io](https://socket.io/)
    * [sample code](https://github.com/socketio/socket.io/tree/master/examples/chat)
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
