import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
list = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rank = 0
for music in list:
    a_tag= music.select_one('td > a')
    if a_tag is not None:
        rank = rank + 1
        title = music.select_one('a.title.ellipsis').text.strip()
        artist = music.select_one('a.artist.ellipsis').text.strip() 
                
        print(rank,title,artist)