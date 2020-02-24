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


def thread_and_res(string):#スレッド名とレス数を返す
    #print(string) #test
    #頭3つの文字列だけのやつを切り捨てる
    if len(string.split(" ",1)) == 1:
        return None
    title = string.split(" ",1)[1]#スレ順を切り捨てる
    if title[-3] == '(':#レス数の桁が違うと文字列が切り取れない不具合があったのでレス数を判定
        title,number = title[:-3],title[-3:]#スレタイとレス数に分割する
    elif title[-4] == '(':
        title,number = title[:-4],title[-4:]#スレタイとレス数に分割する
    elif title[-5] == '(':
        title,number = title[:-5],title[-5:]#スレタイとレス数に分割する
    
    number = re.findall("\((.*)\)",number)#レス数を数字にする
    
    return title, int(number[0])

#warnings.simplefilter("ignore")

url = "http://swallow.5ch.net/livejupiter/subback.html"
#url = "http://example.com/"
#nanJ thread list

html = requests.get(url)
#kore dato mojibake suru
html.encoding = html.apparent_encoding
#moji code wo nantoka sita
#print(type(html.text))


soup = BeautifulSoup(html.text)

name = soup.find_all("a")

for na in name:#この文すごい
    temp = na.get_text()
    #print(temp)
    print(thread_and_res(temp))

st = "1: 123123123(2)"



# #num = re.findall("\((.*)\)")