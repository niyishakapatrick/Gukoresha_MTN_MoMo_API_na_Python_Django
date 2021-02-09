import http.client, urllib.request, urllib.parse, urllib.error, base64
import uuid
import json

x_Reference_Id =  str(uuid.uuid4())
print(x_Reference_Id)

def api_user():
    headers = {
    # Request headers
    'X-Reference-Id': x_Reference_Id,
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9e82c5f1eb524ea19b9e68f5a7b3b473',
    }

    params = urllib.parse.urlencode({
    })

    body = json.dumps({"providerCallbackHost": "itike.pythonanywhere.com" })

    try:
        conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
        conn.request("POST", "/v1_0/apiuser?%s" % params, body, headers)
        response = conn.getresponse()
        print('Response status :',response.status)
        print('Response reason :',response.reason)
        data = response.read()
        print(f'response : {response}, data :{data}')
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

api_user()