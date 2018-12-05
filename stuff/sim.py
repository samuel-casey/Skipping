import requests
import time
# response = requests.get('https://finance.yahoo.com/'
def sim(symbol):
    def pricer(symbol):
        tok = "97b4bdc92aab46aeabb226317b66f0d8"
        params = {'token':tok}
        url="https://api.iextrading.com/1.0/stock/"
        price = requests.get(url+symbol+"/price").json()
        return price
    price = pricer(symbol)
    # time.sleep(3)
    newprice = pricer(symbol)
    if newprice <= 2.08:
        print('buy')
    if newprice >= 2.12:
        print('sell')
    print(price, newprice)
    sim(symbol)
sim('MBII')

key = 'SNO26B13JK1I2CR9'
# 20 period on 5 min
# def sma(symbol, interval)