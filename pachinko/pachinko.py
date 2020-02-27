# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:22:57 2019
@author: 1
"""
import sys
import requests
import re
from bs4 import BeautifulSoup
import warnings
import csv
import pprint
import time

warnings.simplefilter("ignore")
url = "https://papimo.jp/h/00061833/hit/view/816/20200225"

html = requests.get(url)
html.encoding = html.apparent_encoding
soup = BeautifulSoup(html.text)
name = soup.find_all("td")

days=["本日","1日前","2日前"]

for day in days:
	flag=0
	cnt=0
	for i in name:
		if cnt == 7:
			break
		if flag == 1:
			print(i.get_text())
			cnt+=1
		if i.get_text() == day:
			flag=1
			print(day)

	