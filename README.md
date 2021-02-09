# MTN MoMo API with python django
## Refer to documentation from https://momodeveloper.mtn.com/ for more details.


#The provided codes are test on Sandbox (not to be used in production). The codes must be executed in the following order:


###1. sign up/login to https://momodeveloper.mtn.com/
###2. Go to products links and subscribe 
###3. Get product primary key

# Generate API User ID
###1. copy the product primary key and paste it into the api_user_id.py file
###2. add your domain name into the api_user_id.py file
###2. python3 api_user_id.py 

# Generate API Key
###1. copy the product primary key and paste it into api_user_key.py file
###2. copy the API User ID generated from the first step and pasto into api_user_key.py file
###2. python3 api_user_key.py

# Generate token (JWT)
###1. copy the API user ID  and paste it into api_user_token.py file
###2. copy the API KEY  and paste it into api_user_token.py file
###3. copy the product primary key and paste it into api_user_token.py file
###4. add your domain name into the api_user_token.py file
###5. python3 api_user_token.py

# Request to Pay
###1. copy the token obtained from api_user_token.py and paste it into api_user_requestpay.py file
###2. copy the API user ID  and paste it into api_user_requestpay.py file
###3. copy the product primary key and paste it into api_user_requestpay.py file 
###4. add mtn cell number (sould start by 250). don't use +250 or 00250
###5. python3 api_user_token.py






#