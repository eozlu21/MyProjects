
import json
import urllib.request, urllib.parse

serviceUrl = "http://py4e-data.dr-chuck.net/json?"
address = input("Please enter an adress: ")

parms = dict()
parms['address'] = address
parms['key'] = 42

url = serviceUrl + urllib.parse.urlencode(parms)

urlHandle = urllib.request.urlopen(url)
data = urlHandle.read().decode()
# DO NOT FORGET THIS PART!!
myJson = json.loads(data)
# print(json.dumps(myJson))
print(myJson["results"][0]["place_id"])
