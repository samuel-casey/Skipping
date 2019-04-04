import requests

def get_stock_data(stock_symbol, start_date, end_date):
    base_url='https://marketdata.websol.barcharts.com/getHistory.json'
    api_key='b94fc281ade27e76c128346473007b2e'
    params = {'apikey':api_key, 'symbol':stock_symbol, 'type':'daily', 'startDate':start_date, 'endDate': end_date}
    data_response = requests.get(base_url, params)
    print(data_response.url)
    return data_response.json()

print(get_stock_data('MSFT', '20180214', '20180214'))