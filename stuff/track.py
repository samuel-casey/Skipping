# import openpyxl
import bs4
import requests
# import os
# import sys



def yearfinder():

    url = 'https://m.usps.com/m/TrackConfirmAction'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    print(soup)
    span = '#results > ul > li > div.text-description > h2 > a'
    elem = soup.select(span)
    print(elem)

yearfinder()