# Banting Bot - Personal Slack chatbot
# by Riyaad Ali
# Module 1 - Son's Soccer Schedule

from bs4 import BeautifulSoup
from bot import Slacker
import requests
import time

t = time.localtime()
month_day = time.strftime('%b %d', t)

month_day = "Nov 27" # For testing

soccerURL = "https://registration.sportsavvy.com/OVL/index.php"

# POST data for soccer site
soccerPOST = {'YKey': '633',
        'LKey' : '4274',
        'DKey' : '7479',
        'TKey' : '25261',
        'option' : 'com_sportsavvy',
        'controller' : 'schedule' }     

soccerRequest = requests.post(url = soccerURL, data = soccerPOST)
soup = BeautifulSoup(soccerRequest.text, "lxml")

for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    if month_day in str(tds[0]):
       field = str(tds[6]).replace("<td>PGI-","").replace("</td>","")          
          
slacker = Slacker()
slacker.sendMessage("Your son's soccer field - %s" % field, "Today your son will be playing on field *%s*" % field)

          
