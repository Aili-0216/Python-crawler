import requests
import json


def english_china_trans():
    # 1.指定url
    post_url = "https://fanyi.baidu.com/sug"
    # 2.UA伪装反反爬
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0"
                      "Safari/537.36 Edg/120.0.0.0"  # UA伪装反反爬
    }
    # 3.设置参数
    x = input("请输入想要翻译的英文:\n")
    data = {  # 参数
        'kw': x
    }
    # 4.请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.Content-Type:application/json响应数据为 json
    # json()方法直接返回的是一个对象(如果确认响应数据为json时,才可以使用该方法)
    html = response.text  # dumps将python转换为json，loads将json转换为python
    data = json.loads(html)
    print(data)
    # print(type(html))
    # json()本身就是一个字符串，与字典不同的是输出字典需要将字典内的元素通过String方法一个个输出，而json数据本身为字符串类型就不用
    j = 1
    for i in data['data']:
        print(f"{j}" + '\t' + i['k'])
        print(i['v'])
        j = j + 1


english_china_trans()
