import requests
import json


def parse(text):  # 提取数据
    # print(type(text))
    dictdata = json.loads(text)  # 将返回json数据转化为字典
    # print(dictdata)
    # print(dictdata['Table1'])
    # print(type(dictdata))
    for i in dictdata['Table1']:
        print(i['rownum'])
        print("餐厅名称:" + i['storeName'])
        print("餐厅地址:" + i['addressDetail'])
        print("详细扩展:" + str(i['pro']))  # 字符串只能和字符串连接，但是有些店无详细扩展内容，所以值为None，因此需要将其转化为字符串
        print("省份:" + i['provinceName'])
        print("城市名:" + i['cityName'])


def rts():
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
            "Safari/537.36 Edg/120.0.0.0",
        "Cookie":
            "route-cell=ksa; ASP.NET_SessionId=zymcic1kdg21ofi3hbzeserr; "
            "VOLCALB=8af55abb9b149dce32e07be8ff9851e0|1706076345|1706076050; "
            "VOLCALBCORS=8af55abb9b149dce32e07be8ff9851e0|1706076345|1706076050       ",
        "Referer":
            "https://www.kfc.com.cn/kfccda/storelist/index.aspx"
    }
    x = input("输入城市名：")
    for i in range(1, 11):
        url_data = {
            # 全部参数都要加上去即使为空
            'op': 'keyword',
            'cname': '',
            'pid': '',
            'keyword': x,
            'pageIndex': i,
            'pageSize': 10,
        }
        url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
        print(url)
        response = requests.post(url=url, data=url_data, headers=headers)  # f-string为字符串格式方法，就是对字符串进行修改
        # print(response)
        # print(response.status_code)
        html = response.text
        # print(type(html))
        # print(html)
        parse(html)


rts()
