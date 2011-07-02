import httplib, urllib

arduino = httplib.HTTPConnection("192.168.1.40")

try:
	arduino.request("GET","/a0")
	response = arduino.getresponse()
	print "Arduino response:" , response.status, response.reason
	data = response.read()
	print data
except:
	print "Arduino connection failed!"


