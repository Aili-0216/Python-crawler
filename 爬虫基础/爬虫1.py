import requests

url = "https://ie.sogou.com/features/images/features_logo.png"
response = requests.get(url)
data = response.text
print(data)
with open("C:/Users/aili/Desktop/python/sougou.html", "w", encoding='utf-8') as file:
    file.write(data)
