


import requests
URL_TOTAL_LIST = 'https://comic.naver.com/webtoon/weekday.nhn'
response = requests.get(URL_TOTAL_LIST)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')

class_title_a_list = soup.select('a.title')
len(class_title_a_list)

diction={}
for i in class_title_a_list:
   diction[i['title']] = i['href']

input_title = input("웹툰 제목 :")
try:
    w_href = requests.get('https://comic.naver.com{0}'.format(diction[input_title]))
    # w_href = requests.get('https://comic.naver.com{0}'.format(diction['신의 탑']))


except KeyError:
      print("입력하신 웹툰이 없습니다.")

soup_t = BeautifulSoup(w_href.text, 'html.parser')

wrt_name = soup_t.select('span.wrt_nm')[0].text.strip()
wrt_detail = soup_t.select('div.comicinfo > div.detail > p:nth-child(2)')[0].text.strip()
wrt_genre = soup_t.select('span.genre')[0].text.strip()
print('웹툰 명 : ' + input_title)
print('작가명 : ' + wrt_name)
print('웹툰 설명 : ' +wrt_detail)
print('웹툰 장르 : ' + wrt_genre)