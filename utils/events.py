from collections import defaultdict
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def scrap_earnings():
    today = datetime.now().date()
    today = today + timedelta(days=1)
    m = defaultdict(set)
    for i in range(1,6):
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
        url=f'https://finance.yahoo.com/calendar/earnings?day={today}'
        response=requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        for item in soup.select('.simpTblRow'):
            try:
                symbol = item.select_one('td[aria-label="Symbol"] a')
                company = item.select('[aria-label*=Company]')[0].get_text()
                m[today.strftime("%m-%d-%Y")].add(f"{symbol.text} - {company}")
            except Exception as e:
                raise e
        today = today + timedelta(days=1)
    return m

def create_earnings_embed(date, companies):
    fields = []
    for company in companies[:25]:
        fields.append({'name': company, 'value': ""})
    return {
        'content': f"# Earning calls for {date}",
        'embeds': [
            {
                'title': f"Companies earning calls on {date}",
                'description': "List of all companies that have earning calls on this date",
                'color': int('800080', 16),  # Red color
                'fields': fields
            }
        ]        
    }