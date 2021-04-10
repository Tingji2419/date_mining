import requests
from bs4 import BeautifulSoup


def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Host': 'movie.douban.com'}  #请求头
    movie_list = []
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)  #构造请求url
        r = requests.get(link, headers=headers)  #请求体，发送网络请求，请求方式为GET
        soup = BeautifulSoup(r.text, 'lxml')   #数据解析
        div_list = soup.find_all('div', class_='star')
        for each in div_list:
            movie = each.text[2:5]
            movie_list.append(movie)
    return movie_list

if __name__ == "__main__":
    movies = get_movies()
    with open('output.csv', 'a', encoding='utf-8') as infofile:
        infofile.write(str(movies) + '\n')
        infofile.flush()
        infofile.close()  #数据存储，存储方式为csv
    print(movies)
