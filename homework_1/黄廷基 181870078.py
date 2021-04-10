from selenium import webdriver
import requests
from bs4 import BeautifulSoup


# 使用谷歌驱动

def open_page(url):
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        #'Host': 'kandian.youth.cn',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive'
    }  # 请求头

    link = url
    r = requests.get(link, headers=headers, timeout=10)  # 请求体，发送网络请求，请求方式为GET
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')  # 数据解析

    news_one = []
    title = soup.find(class_='rich_media_title')
    date = soup.find(class_='rich_media_meta text')
    author = soup.find(class_='laiyuan')
    content = soup.find(class_='rich_media_content')
    pic = soup.find(class_='pgc-img')

    if title is None:   # 第二种网页
        r = requests.get(link, headers=headers, timeout=10)  # 请求体，发送网络请求，请求方式为GET
        r.encoding = 'gb18030'
        soup = BeautifulSoup(r.text, 'lxml')  # 数据解析

        title = soup.find(class_='page_title')
        date = soup.find(id='page_right')
        author = soup.find(id='source_baidu')
        content = soup.find(class_='TRS_Editor')
        pic = soup.find(align='center')

        if title is None:   # 第三种网页
            r = requests.get(link, headers=headers, timeout=10)  # 请求体，发送网络请求，请求方式为GET
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, 'lxml')  # 数据解析
            title = soup.find(id='title')
            date = soup.find(id='pubtime')
            author = soup.find(id='source')
            content = soup.find(id='content')
            pic = soup.find(id='pic')
        news_one.append('新闻链接：' + url)
        if title is not None:
            news_one.append('标题：' + title.text)
        if date is not None:
            news_one.append('日期：' + date.text)
        if author is not None:
            news_one.append('作者：' + author.text)
        if content is not None:
            news_one.append('内容：' + content.text)
        if pic is not None:
            for i in range(0,len(pic)):
                news_one.append('图片链接' + str(i + 1) + '：' + str(pic[i]))
        news_one.append('\n')

    else:    # 第一种网页
        news_one.append('新闻链接：' + url)
        news_one.append('标题：' + title.text)
        news_one.append('日期：' + date.text)
        news_one.append('作者：' + author.text)
        news_one.append('内容：' + content.text)
        if pic is not None:
            pic = pic.find_all('img')
            for i in range(0, len(pic)):
                news_one.append('图片链接' + str(i+1) + '：' + pic[i].attrs['data-tt'] + '\n')
        news_one.append('\n')
    return news_one


def get_news():
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Host': 'search.youth.cn',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive'
    }  # 请求头
    data_list = []
    for j in range(1, 6):

        link = 'http://search.youth.cn/cse/search?q=%E6%96%B0%E5%86%A0%E7%96%AB%E6%83%85&p='+str(j)+'&s=15107678543080134641&entry=1'
        # link = page_url
        r = requests.get(link, headers=headers, timeout=10)  # 请求体，发送网络请求，请求方式为GET
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')  # 数据解析
        search_result = soup.find_all(class_='c-title')

        for i in search_result:
            print(i.contents[1].attrs['href'])
            data_list.append(open_page(i.contents[1].attrs['href']))    # 选择每条新闻的链接进入

    return data_list


if __name__ == "__main__":
    # page_url = open_page()
    news_list = get_news()
    # sys.setdefaultencoding('utf-8')
    with open('news_output.csv', 'a', encoding='gb18030') as infofile:
        for i in range(0, len(news_list)):
            infofile.write(str(news_list[i])+'\n')
            infofile.flush()
        infofile.close()  # 数据存储，存储方式为csv

