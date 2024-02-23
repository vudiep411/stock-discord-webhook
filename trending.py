import requests
import json
from utils.most_active import *
import os
from dotenv import load_dotenv
import sys

load_dotenv()

webhook_url = os.getenv('TRENDING_WEBHOOK')

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

send(create_trending_embbed())