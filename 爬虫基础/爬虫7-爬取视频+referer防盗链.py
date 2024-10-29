import requests

url='https://www.pearvideo.com/videoStatus.jsp'

#referer防盗链与新数据拼接源
video_url_or='https://www.pearvideo.com/video_1796497'

#获取关键字
key_data=video_url_or.split('_')[-1]

#参数
params={
    'contId': key_data
    # 'mrd': 0.7382352496504627
}

#请求头
header={
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'referer':video_url_or
}

#发起请求
res=requests.get(url,params=params,headers=header)

#接收数据
result=res.json()

#获取初始网页url上json文件下的视频url
video_url_old=result['videoInfo']['videos']['srcUrl']

#获取要替换的旧数据
systemTime=result['systemTime']

#拼接新数据
new_data='cont-'+key_data

#拼接成真正的video_url
video_url_new=video_url_old.replace(systemTime,new_data)
# print(video_url_new)

#向视频发起请求，并获取转换的数据
video_response=requests.get(video_url_new,headers=header)
video_result=video_response.content

#读取视频，写入文件
with open ('video1.mp4','wb')as file:
    file.write(video_result)

video_response.close()

