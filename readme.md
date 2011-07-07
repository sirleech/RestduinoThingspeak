## Read an Arduino via REST and upload value to Thingspeak

This is a great way to offload HTTP processing from your Arduino to another computer. 
It's useful when you still want to be able control the Arduino over a web interface 
(in this case via a RESTful web service) for automation application where it's desired
to log data as well as control the device.

### Instructions
- Load your Arduino with this code: 
  -  https://github.com/jjg/RESTduino or 
  -  https://github.com/sirleech/Webduino/tree/master/examples/RESTduino
- Change the IP address in 'log.py' to your Arduino's IP
- Load your Thingspeak API key into a JSON file 'apikey.js'
- Use the 'Modifiers.py' library to apply calculations to the raw sensor data
- If you are using Cron to run load.py, make sure to code an absolute directory to 'apikey.js'

### Example Chart
http://deadlyspore.com/chris/viewFeed.php?feed=826&hours=12
