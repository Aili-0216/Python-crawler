import time
import requests
from lxml import etree


def get_city_name():
    url = 'https://www.kfc.com.cn/kfccda/storelist/index.aspx'

    # 发起请求
    reps = requests.get(url, headers=headers)

    # 获取数据
    result = reps.text

    # 创建etree对象
    tree = etree.HTML(result)

    # 利用xpath方法html路径定向获取对象并赋值给变量
    city_list = tree.xpath('//ul[@class="city_info"]/li')

    # 循环遍历
    for city_name in city_list:

        #获取路径下的文本，无需在开头添加/
        begin_word = city_name.xpath('span/text()')
        name = city_name.xpath('div[@class="city_city"]/a/text()')

        #输出开头拼音与城市名
        print(begin_word[0])
        print("   ".join(name))

def parse(dictdata):# 提取数据
        for i in dictdata['Table1']:

            #判断地址是否为空
            if i['addressDetail'] is None:
                i['addressDetail'] = '地址失效'

            #输出
            # 字符串只能和字符串连接，但是有些店无详细扩展内容，所以值为None，因此需要将其转化为字符串
            print(
                f"""
                {str(i['rownum'])}
                餐厅名称: {i['storeName']}
                餐厅地址: {i['addressDetail']}
                详细扩展:{str(i['pro'])}
                省份: {i['provinceName']}
                城市名: {i['cityName']}
                """
            )




def rts():
    x = input("输入城市名：")
    for i in range(1, 11):
        #设置post参数
        url_data = {
            # 全部参数都要加上去即使为空
            'op': 'cname',
            'cname': x,
            'pid': '',
            'pageIndex': i,
            'pageSize': 10,
        }
        url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"
        #发起请求
        response = requests.post(url=url, data=url_data, headers=headers)

        # html = response.text#返回的是字符串纯文本
        html=response.json()#返回的是字典

        #判断该地区是否有KFC店铺
        if html['Table'][0]['rowcount'] == 0:
            print("抱歉未查询到此处店铺位置")
            return
        else:
            parse(html)

        response.close()
        time.sleep(0.5)



if __name__ == '__main__':
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
            "Safari/537.36 Edg/120.0.0.0"
    }
    get_city_name()
    rts()

#    "https://www.kfc.com.cn/kfccda/storelist/index.aspx"