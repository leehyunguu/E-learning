import urllib.request
from bs4 import BeautifulSoup

#크레듀 웹사이트의 주소는 아래와 같습니다. 
data = urllib.request.urlopen('https://news.nate.com/rank/interest?sc=sisa')


#검색이 용이한 객체를 생성합니다. 
soup = BeautifulSoup(data, 'html.parser')

#<strong class="tit">{기사 제목}</strong>
list = soup.find_all('strong', attrs={'class':'tit'})

for item in list:
        try:
                print(item.get_text().strip())
        except:
                pass 
        
