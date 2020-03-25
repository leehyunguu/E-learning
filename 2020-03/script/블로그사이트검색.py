
from bs4 import BeautifulSoup
import requests
import re 

#블로그에 있는 글의 목록을 가져오기 
req = requests.get('https://leehyunguu.github.io/')
html = req.text 
soup = BeautifulSoup(html, 'html.parser')

#<a href="{경로}" rel="permalink">{제목}
#</a>
blogList = soup.find_all('h2', class_='archive__item-title')
for item in blogList:
        findItem = item.find('a')
        print(findItem.get_text().strip())
