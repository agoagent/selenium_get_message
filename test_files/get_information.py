import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录后才能访问的网页
url = '******'

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'******'

#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

#设置请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

#data
data = {
    'id': '0000000000',
    'className': '******',
    'new_open': 'modal_dialogue',
}

#在发送get请求时带上请求头和cookies
resp = requests.post(url, headers = headers, cookies = cookies , data=data)
        
print(resp.content.decode('utf-8'))
f = open("./获取表单信息.html",'w',encoding='utf-8')
f.write(resp.content.decode('utf-8'))
f.close
