import requests
import json

url = "https://www.fast2sms.com/dev/bulkV2"

# create a dictionary
my_data = {
    # Your default Sender ID
    'sender_id': 'FTWSMS',

    # Put your message here!
    'message': 'This is a test message',

    'language': 'english',
    'route': 'v3',

    # You can send sms to multiple numbers
    # separated by comma.
    'numbers': '8595816749'
}

# create a dictionary
headers = {
    "authorization":"qY5gbfjKo2w8pEXdMuneh1OZWkcUIy3V7HPS4i6QtvLBRrmDGapafwbN2LXrtDKV3ZIej4gx8ysznoH7",
    "Content-Type":"application/json"
}

response = requests.request("POST", url, data=my_data, headers=headers)

returned_msg = json.loads(response.text)

print(returned_msg['message'])