from yahoo_fin.stock_info import get_day_gainers, get_day_losers


def get_top_gainer():
    top_gainers = get_day_gainers().head(5)
    gainers_tuples = [(row['Symbol'], row['% Change']) for index, row in top_gainers.iterrows()]
    return gainers_tuples

def get_top_losers():
    top_losers = get_day_losers().head(5)
    losers_tuples = [(row['Symbol'], row['% Change']) for index, row in top_losers.iterrows()]
    return losers_tuples

def create_top_gain_lose(ticker_lists, message_content="", title="", description="", color=0):
    fields = []
    for sym, per in ticker_lists:
        fields.append({'name': f"{sym}: {per}%", 'value': ""})
    return {
        'content': message_content,
        'embeds': [
            {
                'title': title,
                'description': description,
                'color': color,  # Red color
                'fields': fields
            }
        ]        
    }