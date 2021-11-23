## Banting Bot - Home automation notification system using Slack
# by Riyaad Ali

# Description

Using a Slack webhook, send Slack messages to a pre-configured private channel for the purpose of home automation notifications. The 'bot' module provides function sendMessage('subject', 'message'). A module will be written for each notification type, e.g. weekly reminders, system alerts, etc.

# Dependencies

python-dotenv
bs4
requests
json
slack_sdk

# Included notification module example:

soccer.py - sends me the field number for my son's weekend soccer games. Script run by a cron job executing every Saturday.

# Usage

Import bot and create a Slacker object, send message:

from bot import Slacker

slacker = Slacker()
slacker.sendMessage("This is my subject", "This is my message")

The subject shows up in the Slack message preview windows, and the message shows inside the actual chat room.

