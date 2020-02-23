
"""
Created on Wed Dec 25 23:12:48 2019

@author: 1
"""

import urllib3

from bs4 import BeautifulSoup
html = urllib3.urlopen("http://example.com")
#html = requests.get("http://swallow.5ch.net/livejupiter/subback.html")
print(type(html))
print(html.encoding)

soup = BeautifulSoup(html, "html.parser")


print(soup.a)