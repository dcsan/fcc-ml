# coding: utf-8
# 
# needs python 3.4

import os
GITTER_USER_TOKEN = os.environ.get('GITTER_USER_TOKEN')
# print("using token " + GITTER_USER_TOKEN)

#not using requests library… I just found that urllib worked fine enough… didn't try requests for this one...
import urllib, urllib.request, urllib.parse
import json, re
import pprint
pp = pprint.PrettyPrinter(indent=4)


def loadData():
    #a request that will pull just the last XX messages
    # key after rooms/ is /Help channel id
    req = urllib.request.Request("https://api.gitter.im/v1/rooms/54a2fa80db8155e6700e42c3/chatMessages?limit=100", headers={"Accept": "application/json", "Authorization": "Bearer "+ GITTER_USER_TOKEN })
    resp = urllib.request.urlopen(req)

    respData = resp.read()
    #print(respData)
    data = json.loads(respData.decode("utf-8"))
    return data

# print(data)

def scan(data):
    foundItems = []
    for blob in data:
        # print(blob.keys() )
        text = blob['text']
        # found = re.search('bonfire', text.lower())
        # if (found):
        lowerText = text.lower()
        if "bonfire" in lowerText:
            foundItems.append(text)
        # else:
            # print(text)
            # pp.pprint(text)
    return foundItems


data = loadData()
foundItems = scan(data)

print("------ Bonfires:", len(foundItems))

for item in foundItems:
    print(item)


#check if it was ok...
# print("found bonfires: ", )
