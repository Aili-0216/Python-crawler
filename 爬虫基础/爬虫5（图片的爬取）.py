import requests
import re
from bs4 import BeautifulSoup  # BeautifulSoup是类


def get_requests(text):
    ur = f"https://pic.netbian.com/{text}"
    img_name = re.split(r'/', text)[-1]
    # print(img_name)
    # print(ur)
    htm = requests.get(url=ur)
    img_data = htm.content
    with open(f'C:/Users/aili/Desktop/python/python 爬虫/爬取图片/{img_name}', 'wb') as file:
        file.write(img_data)
