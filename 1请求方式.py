
# 1、GET请求
import requests    # 导入网络请求模块requests
# 发送网络请求
response = requests.get('https://www.baidu.com')
print('响应状态码为：',response.status_code)  # 打印状态码
print('请求的网络地址为：',response.url)          # 打印请求url
print('头部信息为：',response.headers)      # 打印头部信息
print('cookie信息为：',response.cookies)      # 打印cookie信息

# 2、对响应结果进行UTF-8编码，否则网页源码中的中文信息可能出现乱码
response = requests.get('https://www.baidu.com/')
response.encoding='utf-8'    # 对响应结果进行utf-8编码
print(response.text)         # 以文本形式打印网页源码
print(response.encoding)

# 3、爬取二进制数据——下载图片
response = requests.get('https://www.baidu.com/img/bd_logo1.png?where=super')
print(response.content)                # 打印二进制数据
with open('百度logo.png', 'wb')as f:   # 通过open函数将二进制数据写入本地文件
    f.write(response.content)          # 写入

# 4、GET带参请求
#（1）请求地址带参

response = requests.get('http://httpbin.org/get?name=Jack&age=30')
print(response.text)
#(2)配置params参数
data = {'name': 'Michael', 'age': '36'}
response = requests.get('http://httpbin.org/get',params=data)
print(response.text)

#5 、post请求
import json        # 导入json模块
# 字典类型的表单参数
data = {'1': '能力是有限的，而努力是无限的。',
        '2':'星光不问赶路人，时光不负有心人。'}
# 发送网络请求
response = requests.post('http://httpbin.org/post', data=data)
response_dict = json.loads(response.text)      # 将响应数据转换为字典类型
print(response_dict)                             # 打印转换后的响应数据
