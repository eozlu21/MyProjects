
import xml.etree.ElementTree as ET
from urllib.request import urlopen

myURL = input("Please enter the URL: ")
fHandle = urlopen(myURL).read().decode()
things = ET.fromstring(fHandle)
lst = things.findall("comments/comment")
mySum = 0
for item in lst:
    mySum += int(item.find("count").text)
print(mySum)