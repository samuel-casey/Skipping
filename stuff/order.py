import requests
def order(buysell, symbol, shares):
    if buysell.lower() == 'buy':
        print('BUY', symbol, 'FOR',shares,'SHARES')
    elif buysell.lower() == 'sell':
        print('SELL', symbol, 'FOR',shares,'SHARES')
    else:
        prompt = 'Order for', shares, symbol, 'Please enter buy or sell into string now'
        buysell2 = input(str(prompt))
        order(buysell2, symbol, shares)
        
    url = 'https://api.robinhood.com/api-token-auth/'
    params = {'username':'apiispanen1@babson.edu', 'password':'paulrevere31'}
    a = requests.post(url,data = params)
    b = a.json()
    tok = b['token']
    print(tok)
    # url2 = 'https://api.robinhood.com/user/'
    headers = {'Authorization':'Token '+tok}
    url = 'https://api.robinhood.com/accounts/'
    portfolio='https://api.robinhood.com/accounts/5SR91178/'
    # userid = requests.get(url, headers=headers).json()
    # # useinfo= requests.get(url2,headers=headers).json()
    # # userid = useinfo['url']+useinfo['id']
    # print(userid)
    price = requests.get('https://api.robinhood.com/quotes/'+symbol+'/').json()['ask_price']
    print(price)
    url = 'https://api.robinhood.com/orders/'

    inturl = requests.get('https://api.robinhood.com/instruments/?symbol='+symbol).json()['results'][0]['url']
    print('INSTRU: ',inturl)


    params = {
        'account':portfolio, 
        'instrument':inturl,
        'symbol':symbol,
        'type':'market', 
        'time_in_force':'gfd',
        'trigger':'stop',
        'price':price,
        'quantity':shares,
        'side':buysell.lower(),
        'stop_price':stop_price
        } 
        
    # buyer = requests.post(url, data=params,headers = headers).json()
    # print(buyer)

order('buy' , 'DOGE', 1)
