# Banting Bot - Personal Slack chatbot
# by Riyaad Ali
# 'Slacker' Webhook connection module

import requests
import json
from slack_sdk.webhook import WebhookClient
import os

try:
  from dotenv import load_dotenv
  load_dotenv()
  
except:
  print("Error - could not load environment variables. Terminating.")
  exit()

class Slacker():

  def __init__(self):
  
    self.url = os.environ.get('slackhook') # Webhook URL
    self.webhook = WebhookClient(self.url)

  def sendMessage(self,subject,message):
  
    response = self.webhook.send(
        text=subject,
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": message
                }
            }
        ]
    )