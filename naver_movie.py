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
#=======================================
# movie_codes = ['11093']#,'11757']

import requests

headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=188909',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=QGGJ6VZCFL7V4; NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; MM_NEW=1; NFS=2; MM_NOW_COACH=1; nx_ssl=2; csrf_token=8e6fe8b8-f4a9-4936-90c8-3002684b178c',
}


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=188909&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false', headers=headers)

for movie_code in movie_codes:

    params = (
        ('code', movie_code),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

    soup = BeautifulSoup(response.text, 'html.parser')
    lis = soup.select('body > div > div > div.score_result > ul >li')
    qq = []
    # print(soup)
    for li in lis:
        # print(li)
        # print(li.select_one('div.score_reple > p > span').get_text().replace('/n',"").replace('/t',""))
        score = li.select_one('div.star_score > em').get_text()
        # print(score)
        rating = li.select_one('div.score_reple > p > span').get_text().replace('\n',"").replace('\t',"").replace('\r',"")
        qq.append((score,rating))
    print(qq)

# #=========================================
# # 평점 페이지 들어가서 코드부분을 바꿔가면서 

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# movie_codes = ['11093']#,'11757']
# for movie_code in movie_codes:

#     # 특정 웹페이지에 접근하기
#     driver = webdriver.Chrome()
#     # rating_url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=11093&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={rating_page}'
#     url = f'https://movie.naver.com/movie/bi/mi/point.nhn?code={movie_code}#tab'
#     driver.get(url)
#     driver.implicitly_wait(10)
#     driver.switch_to.frame('pointAfterListIframe') # ("id 또는 name")

#     # HTML 코드 가져오기
#     r = driver.page_source
#     # 파싱
#     soup = BeautifulSoup(r, "html.parser")
#     lis = soup.select('body > div > div > div.score_result > ul >li')
#     qq = []
#     for li in lis:
#         # print(li.select_one('div.score_reple > p > span').get_text().replace('/n',"").replace('/t',""))
#         q = li.select_one('div.score_reple > p > span').get_text().replace('\n',"").replace('\t',"")
#         qq.append(q)
#     print(qq)

# #==================================================
