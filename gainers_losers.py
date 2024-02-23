import requests
import json
from utils.volatility import *
from utils.top_gain_lose import *
import os
from dotenv import load_dotenv
import sys

load_dotenv()

webhook_url = os.getenv('WEBHOOK_URL')
if not webhook_url:
    if len(sys.argv) > 1:
        webhook_url = sys.argv[1]
    else:
        print("Error: Please provide a webhook URL as a command line argument or set the WEBHOOK_URL environment variable.")
        sys.exit(1)

def send(message):
    payload = json.dumps(message)
    response = requests.post(webhook_url, data=payload, headers={'Content-Type': 'application/json'})
    if response.status_code < 300:
        print('Message sent successfully!')
    else:
        print(f'Failed to send message. Status code: {response.status_code}')


gainers = get_top_gainer()
description = "Top 5 daily gainer on the stock market. Trade with caution you dumb fuck"
send(create_top_gain_lose(gainers, title="Daily Gainers",
                          description=description, 
                          message_content="# Daily Gainer",
                          color=int('00FF00', 16)
                          ))


losers = get_top_losers()
description = "Top 5 daily losers on the stock market. Trade with caution you dumb fuck"
send(create_top_gain_lose(losers, title="Daily Losers",
                          description=description, 
                          message_content="# Daily Losers",
                          color=int('FF0000', 16)
                          ))