# coding: utf-8
# 
# needs python 3.4

import os
my_APIkey = os.environ.get('GITTER_USER_TOKEN')
print "using token " + my_APIkey

#not using requests library… I just found that urllib worked fine enough… didn't try requests for this one...
import urllib, urllib.request, urllib.parse
import json






exit(1)

#a request that will pull just the last 20 messages
# key after rooms/ is /Help channel id
req = urllib.request.Request("https://api.gitter.im/v1/rooms/54a2fa80db8155e6700e42c3/chatMessages?limit=20", headers={"Accept": "application/json", "Authorization": "Bearer "+myAPIkey})
resp = urllib.request.urlopen(req)

respData = resp.read()
#print(respData)
data = json.loads(respData.decode("utf-8"))
arr = []
for t in range(len(data)):
   m = re.search('bonfire', data[t]['text'].lower())
   if m:
      #at least once
       arr.append(m.group(0))

#check if it was ok...
len(arr)