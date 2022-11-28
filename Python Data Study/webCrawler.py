from urllib.request import urlopen
from bs4 import BeautifulSoup

def findLinkInPosN(n, repeatCount, url = "http://py4e-data.dr-chuck.net/known_by_Melodie.html"):

    repeatCount -= 1
    currentURL = url
    currentHTML = urlopen(currentURL).read()
    soup = BeautifulSoup(currentHTML, "html.parser")
    tags = soup("a")
    targetTag = tags[n-1]

    if repeatCount == 0:
        return targetTag.contents[0]

    else:
        newURL = targetTag.get("href", None)
        return findLinkInPosN(n, repeatCount, newURL)

print(findLinkInPosN(18, 7))