## Connect Arduino to network with RESTduino sketch

This is a great way to offload HTTP processing from your Arduino to another computer. It's great when you still want to be able control the Arduino over a web interface (in this case via a RESTful web service) for say an automation application.

### Instructions
- Load your Arduino with this code: https://github.com/jjg/RESTduino
- Change the IP address in 'log.py' to your Arduino's IP
- Load your Thingspeak API key into a JSON file 'apikey.js'
- If you are using Cron to run load.py, make sure to code an absolute directory to 'apikey.js'
