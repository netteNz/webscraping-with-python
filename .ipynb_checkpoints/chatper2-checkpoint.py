from urllib.request import urlopen
from bs4 import BeautifulSoup, child 

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

from child in bs.find('table',{'id':'gifList'}).children:
    print(child)