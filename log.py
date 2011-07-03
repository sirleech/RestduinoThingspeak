# Connect Arduino to network with RESTduino sketch
# https://github.com/jjg/RESTduino

import httplib, urllib
import json

arduino = httplib.HTTPConnection("192.168.1.40")
# load your API key into a JSON file 'apikey.js'
# and specify the absolute path if running from Cron
f = open('/root/dev/RestduinoThingspeak/apikey.js', 'r')
jsonObj = json.loads(f.read())
apikey = jsonObj['apikey']

try:
	arduino.request("GET","/a0")
	response = arduino.getresponse()
	print "Arduino response:" , response.status, response.reason
	jsonObj = json.loads(response.read())
	a0 = jsonObj['a0']
	print "a0:", a0

	params = urllib.urlencode({'field1': a0,'key':apikey})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	conn.request("POST", "/update", params, headers)
	ts_response = conn.getresponse()
	print "Thingspeak Response:", ts_response.status, ts_response.reason
	conn.close
except:
	print "connection failed!"


