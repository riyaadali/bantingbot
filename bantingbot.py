# Banting Bot
# by Riyaad Ali

import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup

from slack_sdk.webhook import WebhookClient
url = "https://hooks.slack.com/services/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" # Webhook URL
subject = "Good morning from BantingBot" # Subject of alert message
message = "This is my message to send." # Content of alert message

webhook = WebhookClient(url)

def sendMessage(subj,msg):
  
  response = webhook.send(
      text=subj,
      blocks=[
          {
              "type": "section",
              "text": {
                  "type": "mrkdwn",
                  "text": msg
              }
          }
      ]
  )
  
# Get the time

now = datetime.now()

current_time = now.strftime("%H:%M:%S") # Date var



# Module 1 - Noah's Soccer Schedule

soccerURL = "https://registration.sportsavvy.com/OVL/index.php"

# POST data for soccer
soccerPOST = {'YKey': '633',
        'LKey' : '4274',
        'DKey' : '7479',
        'TKey' : '25261',
        'option' : 'com_sportsavvy',
        'controller' : 'schedule' }     

soccerRequest = requests.post(url = soccerURL, data = soccerPOST)
soup = BeautifulSoup(soccerRequest.text, "lxml")

for table in soup.find_all('table'):
    print(table.get('class'))

#pastebin_url = soccerRequest.text
#print("The pastebin URL is:%s"%pastebin_url)




# sendMessage("Morning Update", f"Good morning Riyaad. The time is { current_time }.")