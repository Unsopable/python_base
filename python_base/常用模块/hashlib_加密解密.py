import hashlib

# n = ord("张") ##24352
# print(n)
#
# m1 = ord("王") ###29579
# print(m1)
#
# a = chr(29579)
# print(a) ##王

string1 = "我爱张"
# print(string1.encode('utf-8')) ##b'\xe6\x88\x91\xe7\x88\xb1\xe5\xbc\xa0'
md5 = hashlib.md5(string1.encode('utf-8'))
encryption = md5.hexdigest()
# print(encryption)


import requests

url = 'https://www.baidu.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400"
}

resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
text = resp.text
print(text)

