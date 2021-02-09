#python3  api_user_token.py
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json


api_user = "<your api user id here>" #put your api user ID 
api_key = <"<your api user key here>" #put your api key 
print('Len apkey',len(api_key), 'len apiuserid', len(api_user))
api_user_and_key  = api_user+':'+api_key
#encoded = base64.b64encode(api_user_and_key)
encoded = base64.b64encode(api_user_and_key.encode()).decode()

def get_token():
    headers = {
        # Request headers
        'Authorization': 'Basic '+encoded,
        #add product primary key in the below line where "<product primary key here>" is.
        'Ocp-Apim-Subscription-Key': '<product primary key here>',
    }

    params = urllib.parse.urlencode({
    })
    #add your domain name where "<you domain name here>" is.
    body = json.dumps({"providerCallbackHost": "<your domain name>" })

    try:
        conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
        conn.request("POST", "/collection/token/?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print('Response status :',response.status)
        print('Response reason :',response.reason)
        print(data)
        return
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    finally:
        conn.close()

get_token()
