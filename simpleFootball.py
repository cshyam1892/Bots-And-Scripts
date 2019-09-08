#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

site = "https://www.skysports.com/football/fixtures" 
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, "html.parser")
spans = soup.findAll('span', class_= ['swap-text__target',
                                    'matches__date'])
for span in spans:
    print(span.text)

