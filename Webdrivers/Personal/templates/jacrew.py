import openpyxl
import bs4
import requests
import os
import sys

sys.argv

def price(code):
    url = 'http://www.nasdaq.com/symbol/'+code+'/real-time'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    span = '#qwidget_lastsale'
    elems = soup.select(span)
    elems = float(elems[0].text[1:])
    return elems

def ltc_price():
    url = 'https://coinmarketcap.com/currencies/litecoin/'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    span = '#quote_price > span.text-large2'
    elems = soup.select(span)
    elems = float(elems[0].text.strip())
    return elems



wb = openpyxl.load_workbook('C:/Users/app_acer/Desktop/Documents/Drew Senior/JacrewInvestments.xlsx')
sheet = wb.get_sheet_by_name(wb.get_sheet_names()[0])
for i in range (9): #HOW MANY STOCK ENTRIES YOU GOT???
    code = sheet['B'+str(5+i)].value
    sheet['D'+str(5+i)] = price(code)
sheet['L1'] = ltc_price()
os.chdir('C:\\users\\app_acer\\Desktop\\Documents\\Drew Senior')
if os.path.isfile('Jacrew_Updated.xlsx'):
    os.remove('Jacrew_Updated.xlsx')
    wb.save('Jacrew_Updated.xlsx')
else:
    wb.save('Jacrew_Updated.xlsx')
os.startfile('Jacrew_Updated.xlsx')