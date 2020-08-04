
import requests
from bs4 import BeautifulSoup
import csv

soup_objects = []
# num = 0
base_url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start='
end_url = '&refresh_start=0'
for i in range(1,102,10):
    # num += 1
    # print(num)
    start_num = i

    URL = base_url + str(start_num) + end_url

    response = requests.get(URL)
    # print(response.text)
    # print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup_objects.append(soup)
print(len(soup_objects))
print(type(soup))

for i in soup_objects:
    # print(soup.select('#main_pack > div.news.mynews.section._prs_nws > ul'))
    ul_type01 = soup.select_one('#main_pack > div.news.mynews.section._prs_nws > ul')
    # print(ul_type01[0])
    # print(ul_type01[0].select('li'))
    for a_tag in ul_type01.select('li > dl > dt > a'):
        new_title = a_tag['title']
        new_link = a_tag['href']

        new_data = {"title": new_title, "hyperlink": new_link}

        with open('./naver_news.csv' , 'a', encoding= 'utf-8') as f:
            fieldnames = new_data.keys()
            w = csv.writer(f)
            w.writerow(new_data.values())

        print('===================================')