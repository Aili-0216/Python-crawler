import requests

# 直接从浏览器发起请求的Url拿到的数据并非动态数据
# 通过ajax方法调用别的url来获取数据展示在浏览器，而我们就需要来获取正确的url来对其发起数据请求
# 要爬取的局部详细数据是动态加载数据，即并非靠浏览器的url请求的数据，而是对其他url请求获得的数据
# 详细数据界面的数据也是动态加载数据
url='https://www.nmpa.gov.cn/'
headers = {

    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'referer':'https://cn.bing.com/',
    'cookie':'acw_tc=3ccdc15517289788355392802e0f427b89312c3c7be8425fc59908b28e3cf1; NfBCSins2OywS=60_cfM.ma70OBn2CaMjhno_6YyfQMFLYlRdtrBsFFZlfFILMGONfXOLO8Kkr1SC.DhNRPsN.udIiwBYcTvqT2tUa; arialoadData=true; ariawapChangeViewPort=true; visualdevice=pc; NfBCSins2OywT=0HHWXImP6yBBJzsTsoNmymdyEbZaYpHXHFBwvW1hxJtmkROoHGZqsk2kKsFPZR1M2nVz28Dc8b7BWHY8SiU_JIscU8cnLIG_ZAIIW0xVtXOSmosuKgoRrj0r3.t6eYAdtInMrSq3IcmJQfHiN9pimqWBH5m3oHGWzmUkIncNBU2AQdd9E3uwKPII8JF3_Z.CP2edKDN0YSUwkGKuzOdyOEtXJsnG2W05XO3YjAKYbpE6p4MsmvFjnaYUdza7e3uQQLKr5aKyzfqs2SgsbuiM_z5PGmpJH9M9zet5PyLzDI2PNhlZAsm.0tkPOzjcpJpBX_BTeripPFSghQW5CW85yVdXlJntcO8vQI5sLYV9m.xl'

}
res = requests.get(url=url, headers=headers)
res.encoding=res.apparent_encoding
res_result=res.text
res.close()
print(res_result)
