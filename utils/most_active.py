from bs4 import BeautifulSoup
import requests

def get_most_active():
    most_active = []
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url='https://finance.yahoo.com/most-active/'
    response=requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    for item in soup.select('.simpTblRow'):
        try:
            symbol = item.select('[aria-label=Symbol]')[0].get_text()
            price = item.select('[aria-label*=Price]')[0].get_text()
            most_active.append((symbol, price))
        except Exception as e:
            raise e
    return most_active

def create_trending_embbed():
    ticker_lists = get_most_active()
    fields = []
    for sym, price in ticker_lists:
        fields.append({'name': f"{sym}: ${price}", 'value': ""})
    return {
        'content': "# Most active",
        'embeds': [
            {
                'title': "Most Active Daily",
                'description': "Most active ticker traded on the market",
                'color': int('FFFF00', 16),  # Red color
                'fields': fields
            }
        ]        
    }
