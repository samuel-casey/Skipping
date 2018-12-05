# import openpyxl
import bs4
import requests
# # import os
# # import sys


def yearfinder():
    y = "2016"
    m = "12"
    d = "25"

    code = y+"/"+m+"/"+d
    url = 'http://www.columbiapipeinfo.com/infopost/Default.aspx?info=Y'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    span = '#obsTable'
  
    # elems = soup.select(span)
    print(soup) 
    # datasets = []
    # for row in table.find_all("tr")[1:]:
    # dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    # datasets.append(dataset)

yearfinder()