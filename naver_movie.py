import requests
from bs4 import BeautifulSoup
import re 

#  a 태그에 영화 코드 가져와서 리스트에 담기 
url = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movie_section = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')
#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dt > a')

# print(soup)
# print(response)
# print(movie_section)

movie_titles = []
movie_codes = []
movie_data = []
for li in movie_section:
    a = li.select_one('div.thumb > a')
    a_href = a['href']
    # print(a_href.find('='))
    _code = a_href[28:]
    print(_code)

    # print(li)
    tit_a = li.select_one('dl.lst_dsc > dt.tit > a').get_text()
    # print(tit_a.get_text())
    m_dict = {}
    m_dict['title'] = tit_a
    m_dict['code'] = _code
    movie_data.append(m_dict)
    movie_titles.append(tit_a)
    movie_codes.append(_code)
# print(movie_titles)
# print(len(movie_titles))

# print(movie_codes)
# print(len(movie_codes))
print(movie_data)

# 평점 페이지 들어가서 코드부분을 바꿔가면서 
# 
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# movie_codes = ['11093']#,'11757']
# for movie_code in movie_codes:

#     # 특정 웹페이지에 접근하기
#     driver = webdriver.Chrome()
#     url = f'https://movie.naver.com/movie/bi/mi/point.nhn?code={movie_code}#tab'
#     driver.get(url)
#     driver.implicitly_wait(10)

#     # HTML 코드 가져오기
#     r = driver.page_source
#     # 파싱
#     soup = BeautifulSoup(r, "html.parser")
#     rating_section = soup.select('div.ifr_module2')
#     print(rating_section)





