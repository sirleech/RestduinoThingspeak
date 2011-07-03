# Connect Arduino to network with RESTduino sketch
# https://github.com/jjg/RESTduino

import httplib, urllib
import json

arduino = httplib.HTTPConnection("192.168.1.40")

try:
	arduino.request("GET","/a0")
	response = arduino.getresponse()
	print "Arduino response:" , response.status, response.reason
	json = json.loads(response.read())
	a0 = json['a0']
	print "a0:", a0

	params = urllib.urlencode({'field1': a0,'key':'6Z6I1R4JT1YK6L9F'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	conn.request("POST", "/update", params, headers)
	ts_response = conn.getresponse()
	print "Thingspeak Response:", ts_response.status, ts_response.reason
	conn.close
except:
	print "connection failed!"


