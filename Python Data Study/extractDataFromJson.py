
import json
import urllib.request, urllib.parse

myURL = input("Please enter the .json adress: ")
recievedHTML = urllib.request.urlopen(myURL)
data = recievedHTML.read().decode()
myJson = json.loads(data)
# print(json.dumps(myJson))
mySum = 0
for person in myJson["comments"]:
    mySum += person["count"]
print(mySum)