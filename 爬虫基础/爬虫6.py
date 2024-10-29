import requests
from lxml import etree
url='https://www.kfc.com.cn/kfccda/storelist/index.aspx'

headers={
"User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
            "Safari/537.36 Edg/120.0.0.0"
}

reps=requests.get(url,headers=headers)
result =reps.text
tree=etree.HTML(result)
city_list=tree.xpath('//ul[@class="city_info"]/li')
for city_name in city_list:
    begin_word = city_name.xpath('span/text()')
    name=city_name.xpath('div[@class="city_city"]/a/text()')#无需在开头加/
    print(begin_word[0])
    print("   ".join(name))
