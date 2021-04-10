import requests    # 导入网络请求模块requests

# 1、添加请求头
url = 'https://www.baidu.com/'     # 创建需要爬取网页的地址
# 创建头部信息
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}
response = requests.get(url, headers=headers)    # 发送网络请求
print(response.status_code)  # 打印响应状态码
print(response.text)

# 对比
response = requests.get(url)    # 发送网络请求
response.encoding='utf-8'
print(response.status_code)  # 打印响应状态码
print(response.text)

#2、cookies设置
from lxml import etree  # 导入lxml模块

cookies = '此处填写登录后网页中的cookie信息'
headers = {'Host': 'www.douban.com',
           'Referer': 'https://www.hao123.com/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/72.0.3626.121 Safari/537.36'}
# 创建RequestsCookieJar对象，用于设置cookies信息
cookies_jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    cookies_jar.set(key, value)  # 将cookies保存RequestsCookieJar当中
# 发送网络请求
response = requests.get('https://www.douban.com/',
headers=headers, cookies=cookies_jar)
if response.status_code == 200:  # 请求成功时
    html = etree.HTML(response.text)  # 解析html代码
    # 获取用户名
    name = html.xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]/text()')
    print(name[0])  # 打印用户名

# 3、异常处理
import requests     # 导入网络请求模块
# 循环发送请求50次
for a in range(0, 10):
    try:    # 捕获异常
        # 设置超时为0.01秒
        response = requests.get('https://www.baidu.com/', timeout=0.03)
        print(response.status_code)                                        # 打印状态码
    except Exception as e:                                                 # 捕获异常
        print('异常'+str(e))                                                # 打印异常信息

#4、异常捕获
import requests  # 导入网络请求模块
# 导入requests.exceptions模块中的三种异常类
from requests.exceptions import ReadTimeout,HTTPError,RequestException
# 循环发送请求50次
for a in range(0, 50):
    try:    # 捕获异常
        # 设置超时为0.1秒
        response = requests.get('https://www.baidu.com/', timeout=0.1)
        print(response.status_code)                                        # 打印状态码
    except ReadTimeout:                                                     # 超时异常
        print('timeout')
    except HTTPError:                                                       # HTTP异常
        print('httperror')
    except RequestException:                                               # 请求异常
         print('reqerror')