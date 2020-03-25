# web01.py
import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('http://www.google.com')

# 검색이 용이한 soup객체를 생성합니다.
soup = BeautifulSoup(page, 'html.parser')

# <td>태그를 검색한다.
print(soup.find_all('td'))