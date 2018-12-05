import requests
import pprint

# url = 'https://api.robinhood.com/api-token-auth/'
# # a = requests.get(url)
# params = {'username':'apiispanen1@babson.edu', 'password':'paulrevere31'}
# a = requests.post(url,data = params)
# b = a.json()
# tok = b['token']
keyword = 'nasdaq'
url2 = 'https://api.robinhood.com/instruments/'
noquery = requests.get(url2)
# ad = noquery.json()['results']
# hidden = [result['name'] for result in ad if result['url']!='https://api.robinhood.com/instruments/50810c35-d215-4866-9758-0ada4ac79ffa/']
# print(hidden)
data = {'query':keyword}
c = requests.get(url2, params=data)
d = c.json()
results = d['results']
for result in results:
    country = result['country']
    name = result['name']
    url = result['url']
    print(country, name, url)
x=0
# while x<10:
#     for thing in d:
#         print(d[thing])
#         x+=1

# results = d['results']
# print(results)
    # print(blank['country'], blank['name'])
# pprint.pprint(results)