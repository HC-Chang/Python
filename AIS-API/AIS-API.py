import json
import urllib.request


data = {
	"nmea":"!AIVDM,1,1,,A,18UG;P0012G?Uq4EdHa=c;7@051@,0*53"
}

# API's Web
myurl = "http://ais.tbsalling.dk/decode"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json')

# Set Data Type as JSON
jsondata = json.dumps(data)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))

# POST & Receive Data
response = urllib.request.urlopen(req, jsondataasbytes) 

# Open JSON Object
response = json.load(response)

# POST Data
print (jsondataasbytes)
# Receive JSON Data
print (response)

