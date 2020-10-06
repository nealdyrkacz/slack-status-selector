import requests
import json
import time

def sendStatus(statusSelection):
    url = 'https://slack.com/api/users.profile.set'
    payload = {"user": "<SLACK_USER_ID>",
               "profile": {
                   "status_text": statusSelection.getMessage(),
                   "status_emoji": statusSelection.getEmoji(),
                   "status_expiration": 0
                   }
               }

    headers = {"Authorization": "Bearer <TOKEN>"}

    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
 
    return
