#python3 api_user_key.py
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    #add product primary key in the below line where "<product primary key here>" is.
    'Ocp-Apim-Subscription-Key': '<product primary key here>',
}

params = urllib.parse.urlencode({
})
#add your domain name "<you domain name here>" is.
body = json.dumps({"providerCallbackHost": "<you domain name here>" })

try:
    conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
    #Add api user ID in the below line where "<api user id here>" is.
    conn.request("POST", "/v1_0/apiuser/<api user id here>/apikey?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print('Response status :',response.status)
    print('Response reason :',response.reason)
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

