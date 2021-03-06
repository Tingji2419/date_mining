
import pickle
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import pymysql
from pymysql.converters import escape_string
import datetime
import csv


# pymysql.install_as_MySQLdb()

chrome_options = Options()
prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_experimental_option('w3c', False)

#MAC版本
#browser = webdriver.Chrome(chrome_options=chrome_options)

#Windows版本
chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  #修改webdriver的绝对位置
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=chrome_driver)

wait = WebDriverWait(browser, 10)
browser.implicitly_wait(1800)


def get_tbshop():
    html = browser.page_source
    if str(html).find("tb-shop-name") != -1:
        str_temp=re.findall('tb-shop-name(.*?)</div>', str(html), re.S)
        shop_name2 =re.findall('title="(.*?)"', str(str_temp), re.S)
        shop_name1 = str(shop_name2).replace("['", "")
        shop_name = str(shop_name1).replace("']", "")

        shop_url2 =re.findall('href="(.*?)"', str(str_temp), re.S)
        shop_url1 = str(shop_url2).replace("['", "")
        shop_url = str(shop_url1).replace("']", "")

        str_temp1=re.findall('"tb-shop-age"(.*?)</div>', str(html), re.S)
        shop_age1=re.findall('tb-shop-age-val">(.*?)</span>', str(str_temp1), re.S)
        shop_age2=re.findall('tb-shop-age-desc">(.*?)</span>', str(str_temp1), re.S)
        shop_age4 = str(shop_age1).replace("['", "")
        shop_age5 = str(shop_age4).replace("']", "")
        shop_age6 = str(shop_age2).replace("['", "")
        shop_age7 = str(shop_age6).replace("']", "")
        shop_age3 =str(shop_age5)+str(shop_age7)

        str_temp2=re.findall('tb-shop-seller(.*?)</div>', str(html), re.S)
        shop_seller2 =re.findall('title="掌柜:(.*?)"', str(str_temp2), re.S)
        shop_seller1 = str(shop_seller2).replace("['", "")
        shop_seller = str(shop_seller1).replace("']", "")

        str_temp3=re.findall('tb-shop-icon(.*?)</div>', str(html), re.S)
        shop_qua1=re.findall('target="_blank"(.*?)</a>', str(str_temp3), re.S)
        shop_qua3 = re.findall('title="(.*?)"', str(shop_qua1), re.S)
        shop_qua4 = str(shop_qua3).replace("['", "")
        shop_qua2 = str(shop_qua4).replace("']", "")

        str_temp4=re.findall('tb-shop-rate(.*?)</div>', str(html), re.S)
        shop_rate1=re.findall('class="tb-rate-higher"(.*?)</dd>', str(str_temp4), re.S)
        shop_rate2 = re.findall('">(.*?)</a>', str(shop_rate1), re.S)
        shop_rate3 = str(shop_rate2).replace(" ", "")
        shop_rate4 = str(shop_rate3).replace("\\n", "")
        shop_rate6 = str(shop_rate4).replace("\\", "")
        shop_rate7 = str(shop_rate6).replace("['", "")
        shop_rate5 = str(shop_rate7).replace("']", "")
    else:
        if str(html).find("shop-name-wrap") != -1:
            str_temp = re.findall('class="shop-name-link"(.*?)<span', str(html), re.S)
            shop_name4 = re.findall('">(.*?)</a>', str(str_temp), re.S)
            shop_name3 = str(shop_name4).replace("\\n", "")
            shop_name2 = str(shop_name3).replace("\\", "")
            shop_name5 = str(shop_name2).replace(" ", "")
            shop_name6 = str(shop_name5).replace("['", "")
            shop_name = str(shop_name6).replace("']", "")

            shop_url2 = re.findall('href="(.*?)"', str(str_temp), re.S)
            shop_url1 = str(shop_url2).replace("['", "")
            shop_url = str(shop_url1).replace("']", "")

            shop_age3 = ""

            str_temp2 = re.findall('shop-more-info(.*?)</div>', str(html), re.S)
            shop_seller4 = re.findall('柜：(.*?)<p', str(str_temp2), re.S)
            shop_seller3 = re.findall('</span>(.*?)</p>', str(shop_seller4), re.S)
            shop_seller2 = str(shop_seller3).replace("\\n", "")
            shop_seller1 = str(shop_seller2).replace("\\", "")
            shop_seller5 = str(shop_seller1).replace(" ", "")
            shop_seller6 = str(shop_seller5).replace("['", "")
            shop_seller = str(shop_seller6).replace("']", "")

            str_temp3 = re.findall('质：(.*?)</p>', str(str_temp2), re.S)
            shop_qua4 = re.findall('title="(.*?)"', str(str_temp3), re.S)
            shop_qua3 = str(shop_qua4).replace("['", "")
            shop_qua2 = str(shop_qua3).replace("']", "")

            str_temp4 = re.findall('class="shop-dynamic-score"(.*?)</div>', str(html), re.S)
            shop_rate1 = re.findall('<em(.*?)em>', str(str_temp4), re.S)
            shop_rate2 = re.findall('">(.*?)</', str(shop_rate1), re.S)
            shop_rate3 = str(shop_rate2).replace(" ", "")
            shop_rate4 = str(shop_rate3).replace("\\n", "")
            shop_rate6 = str(shop_rate4).replace("\\", "")
            shop_rate7 = str(shop_rate6).replace("['", "")
            shop_rate5 = str(shop_rate7).replace("']", "")
        else:
            shop_name=""
            shop_url=""
            shop_age3=""
            shop_seller=""
            shop_qua2=""
            shop_rate5=""
            print("店铺信息爬取出现问题")
    global url

    shop_name = escape_string(str(shop_name))
    shop_url = escape_string(str(shop_url))
    shop_age3 = escape_string(str(shop_age3))
    shop_seller = escape_string(str(shop_seller))
    shop_qua2 = escape_string(str(shop_qua2))
    shop_rate5 = escape_string(str(shop_rate5))
    url = escape_string(str(url))
    #保存内容
    sql = "insert into shop values (\'%s\'"
    for i in range(6):
        sql += ",\'%s\'"
    sql += ")"
    cur.execute(sql % (shop_name,shop_url,shop_age3,shop_seller,shop_qua2,shop_rate5,url))
    print(str("店铺信息爬取成功"))

def get_tbproduct():
    global url
    html = browser.page_source

    str_temp=re.findall('tb-main-title(.*?)class="tb-subtitle"', str(html), re.S)
    pro_name=re.findall('">(.*?)</h3>', str(str_temp), re.S)
    pro_name1 = str(pro_name).replace(" ", "")
    pro_name2 = str(pro_name1).replace("\\n", "")
    pro_name4 = str(pro_name2).replace("\\", "")
    pro_name5 = str(pro_name4).replace("['", "")
    pro_name3 = str(pro_name5).replace("']", "")

    str_temp1=re.findall('tb-rmb-num(.*?)</strong>', str(html), re.S)
    pro_price2 =re.findall('">(.*?)</em>', str(str_temp1), re.S)
    pro_price1 = str(pro_price2).replace("['", "")
    pro_price = str(pro_price1).replace("']", "")

    if str(html).find("wl-servicetitle") != -1:
        str_temp2=re.findall('wl-servicetitle(.*?)</s>', str(html), re.S)
        if str(str_temp2).find("</span>") != -1:
            pro_freight2 =re.findall('</span>(.*?)<s>', str(str_temp2), re.S)
            pro_freight1 = str(pro_freight2).replace("['", "")
            pro_freight = str(pro_freight1).replace("']", "")
        else:
            pro_freight2 = re.findall('">(.*?)<s>', str(str_temp2), re.S)
            pro_freight1 = str(pro_freight2).replace("['", "")
            pro_freight = str(pro_freight1).replace("']", "")
    else:
        pro_freight = "null"

    str_temp3=re.findall('tb-extra(.*?)</div>', str(html), re.S)
    pro_promise1=re.findall('承诺(.*?)</dd>', str(str_temp3), re.S)
    pro_promise2 = re.findall('title="(.*?)"', str(pro_promise1), re.S)
    pro_promise1 = str(pro_promise2).replace("['", "")
    pro_promise = str(pro_promise1).replace("']", "")

    pro_pay1=re.findall('支付(.*?)</dd>', str(str_temp3), re.S)
    pro_pay2 = re.findall('<img(.*?)a>', str(pro_pay1), re.S)
    pro_pay3 = re.findall('>(.*?)</', str(pro_pay2), re.S)
    pro_pay4 = str(pro_pay3).replace("['", "")
    pro_pay = str(pro_pay4).replace("']", "")

    str_tbclick = browser.find_element_by_css_selector("#J_ServiceTab > a")
    str_tbclick.click()
    time.sleep(3)
    html=browser.page_source

    str_temp4=re.findall('kg-contract(.*?)</ul>', str(html), re.S)
    pro_service1=re.findall('class="name"(.*?)h3>', str(str_temp4), re.S)
    pro_service2 = re.findall('>(.*?)</', str(pro_service1), re.S)
    pro_service3 = str(pro_service2).replace("['", "")
    pro_service = str(pro_service3).replace("']", "")

    str_temp5=re.findall('J_FavCount(.*?)</a>', str(html), re.S)
    pro_collect1=re.findall('">(.*?)</em>', str(str_temp5), re.S)
    pro_collect2 = str(pro_collect1).replace("(", "")
    pro_collect3 = str(pro_collect2).replace("人气)", "")
    pro_collect4 = str(pro_collect3).replace("['", "")
    pro_collect = str(pro_collect4).replace("']", "")

    pro_review_num2=re.findall('J_RateCounter">(.*?)</strong>', str(html), re.S)
    pro_review_num1 = str(pro_review_num2).replace("['", "")
    pro_review_num = str(pro_review_num1).replace("']", "")
    if pro_review_num == "[]":
        pro_review_num = 0
    else:
        pro_review_num = pro_review_num

    pro_sell_num2=re.findall('J_SellCounter">(.*?)</strong>', str(html), re.S)
    pro_sell_num1 = str(pro_sell_num2).replace("['", "")
    pro_sell_num = str(pro_sell_num1).replace("']", "")

    str_tbclick = browser.find_element_by_css_selector("#J_TabBar > li:nth-child(2) > a")
    str_tbclick.click()
    time.sleep(3)
    html=browser.page_source

    str_temp=re.findall('data-kg-rate-stats="pic"(.*?)span>', str(html), re.S)
    re_pic_num1=re.findall('>(.*?)</', str(str_temp), re.S)
    re_pic_num2 = str(re_pic_num1).replace("(", "")
    re_pic_num3 = str(re_pic_num2).replace(")", "")
    re_pic_num4 = str(re_pic_num3).replace("['", "")
    re_pic_num = str(re_pic_num4).replace("']", "")

    str_temp1=re.findall('data-kg-rate-stats="good"(.*?)span>', str(html), re.S)
    re_good_num1=re.findall('>(.*?)</', str(str_temp1), re.S)
    re_good_num2 = str(re_good_num1).replace("(", "")
    re_good_num3 = str(re_good_num2).replace(")", "")
    re_good_num4 = str(re_good_num3).replace("['", "")
    re_good_num = str(re_good_num4).replace("']", "")

    str_temp2=re.findall('data-kg-rate-stats="neutral"(.*?)span>', str(html), re.S)
    re_neutral_num1=re.findall('>(.*?)</', str(str_temp2), re.S)
    re_neutral_num2 = str(re_neutral_num1).replace("(", "")
    re_neutral_num3 = str(re_neutral_num2).replace(")", "")
    re_neutral_num4 = str(re_neutral_num3).replace("['", "")
    re_neutral_num = str(re_neutral_num4).replace("']", "")

    str_temp3=re.findall('data-kg-rate-stats="bad"(.*?)span>', str(html), re.S)
    re_bad_num1=re.findall('>(.*?)</', str(str_temp3), re.S)
    re_bad_num2 = str(re_bad_num1).replace("(", "")
    re_bad_num3 = str(re_bad_num2).replace(")", "")
    re_bad_num4 = str(re_bad_num3).replace("['", "")
    re_bad_num = str(re_bad_num4).replace("']", "")

    if str(html).find("data-kg-rate-stats=\"append\"") != -1:
        str_temp4 = re.findall('data-kg-rate-stats="append"(.*?)span>', str(html), re.S)
        re_append_num1 = re.findall('>(.*?)</', str(str_temp4), re.S)
        re_append_num2 = str(re_append_num1).replace("(", "")
        re_append_num3 = str(re_append_num2).replace(")", "")
        re_append_num4 = str(re_append_num3).replace("['", "")
        re_append_num = str(re_append_num4).replace("']", "")
    else:
        re_append_num=""
        pass

    if str(html).find("charityTreasure") != -1:
        str_temp5 = re.findall('charityTreasure(.*?)attributes', str(html), re.S)
        charityTreasure1 = re.findall('class="brief"(.*?)</p>', str(str_temp5), re.S)
        charityTreasure4=re.findall('<strong>(.*?)</strong>', str(charityTreasure1), re.S)
        charityTreasure6=re.findall('class="field"(.*?)</a>', str(str_temp5), re.S)
        charity_name=charityTreasure4[0]
        charity_price=charityTreasure4[1]
        if len(charityTreasure4)>2:
            charity_amount=charityTreasure4[2]
        else:
            charity_amount = ""
        charity_detail=re.findall('href="(.*?)"', str(charityTreasure6), re.S)
    else:
        charity_name=""
        charity_price=""
        charity_detail=""
        charity_amount=""
        pass


    input_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    pro_name3 = escape_string(str(pro_name3))
    pro_price = escape_string(str(pro_price))
    pro_freight = escape_string(str(pro_freight))
    pro_promise = escape_string(str(pro_promise))
    pro_pay = escape_string(str(pro_pay))
    pro_service = escape_string(str(pro_service))
    pro_collect = escape_string(str(pro_collect))
    pro_review_num = escape_string(str(pro_review_num))
    pro_sell_num = escape_string(str(pro_sell_num))
    re_pic_num = escape_string(str(re_pic_num))
    re_good_num = escape_string(str(re_good_num))
    re_neutral_num = escape_string(str(re_neutral_num))
    re_bad_num = escape_string(str(re_bad_num))
    re_append_num = escape_string(str(re_append_num))
    charity_name = escape_string(str(charity_name))
    charity_price = escape_string(str(charity_price))
    charity_amount = escape_string(str(charity_amount))
    charity_detail = escape_string(str(charity_detail))
    url = escape_string(str(url))
    input_time = escape_string(str(input_time))
    #保存内容
    sql = "insert into product values (\'%s\'"
    for i in range(19):
        sql += ",\'%s\'"
    sql += ")"
    cur.execute(sql % (pro_name3,pro_price,pro_freight,pro_promise,pro_pay,pro_service,pro_collect,pro_review_num,pro_sell_num,re_pic_num,re_good_num,re_neutral_num,re_bad_num,re_append_num,charity_name,charity_price,charity_amount,charity_detail,url,input_time))
    print(str("商品信息爬取成功"))
    return(pro_review_num)

def get_tbreview():
    global url
    str_tbclick = browser.find_element_by_css_selector("#J_TabBar > li:nth-child(2) > a")
    str_tbclick.click()
    time.sleep(3)
    html=browser.page_source

    review_num2=re.findall('J_RateCounter">(.*?)</strong>', str(html), re.S)
    review_num1 = str(review_num2).replace("['", "")
    review_num = str(review_num1).replace("']", "")
    a=int(str(review_num))/20+5
    tb_num2 = 0
    for b in range(int(a)):
        time.sleep(3)
        html = browser.page_source
        tmp_str4 = re.findall('class="tb-revbd"(.*?)class="kg-pagination2', str(html), re.S)
        tmp_str3= str(tmp_str4).replace(" ", "")
        tmp_str1= str(tmp_str3).replace("\\n", "")
        tmp_str = re.findall('<li(.*?)</div></li>', str(tmp_str1), re.S)
        tb_num=len(tmp_str)

        for i in range(int(tb_num)):
            #print("正在打印第" + str(tb_num2+i+1)+"条评论")
            cus_id1 = re.findall('id="review-(.*?)"', str(tmp_str[i]), re.S)
            cus_id2 = str(cus_id1).replace("['", "")
            cus_id = str(cus_id2).replace("']", "")

            str_temp = re.findall('class="from-whom"(.*?)class="review-details"', str(tmp_str[i]), re.S)
            cus_name2 = re.findall('<div>(.*?)</div>', str(str_temp), re.S)
            cus_name1 = str(cus_name2).replace("['", "")
            cus_name = str(cus_name1).replace("']", "")

            cus_rank1 = re.findall('class="avatar"(.*?)</div>', str(str_temp), re.S)
            cus_rank2 = re.findall('src="(.*?)"', str(cus_rank1), re.S)
            cus_rank3 = str(cus_rank2).replace("['", "")
            cus_rank = str(cus_rank3).replace("']", "")

            re_content1 = re.findall('class="J_KgRate_ReviewContent(.*?)div>', str(tmp_str[i]), re.S)
            re_content2 = re.findall('">(.*?)</', str(re_content1), re.S)
            re_content3 = str(re_content2).replace("<spanclass=\"tb-tbcr-bracketed\">[追加评论]", "")
            re_content4 = str(re_content3).replace("['", "")
            re_content = str(re_content4).replace("']", "")

            re_pic1 = re.findall('class="tb-rev-item-media"(.*?)</div>', str(tmp_str[i]), re.S)
            if str(re_pic1).find("photo-item") != -1:
                re_pic2 = re.findall('src="(.*?)"', str(re_pic1), re.S)
                re_pic1 = str(re_pic2).replace("['", "")
                re_pic = str(re_pic1).replace("']", "")
            else:
                re_pic = ""

            re_video1 = re.findall('class="tb-rev-item-media"(.*?)</div>', str(tmp_str[i]), re.S)
            if str(re_video1).find("video-item") != -1:
                re_video2 = re.findall('mp4-src="(.*?)"', str(re_video1), re.S)
                re_video1 = str(re_video2).replace("['", "")
                re_video = str(re_video1).replace("']", "")
            else:
                re_video = ""

            if str(tmp_str[i]).find("tb-rev-item-append") != -1:
                re_append = re.findall('tb-rev-item-append(.*?)class="tb-r-act-bar"', str(tmp_str[i]), re.S)
                re_pic1 = re.findall('class="tb-rev-item-media"(.*?)</div>', str(re_append), re.S)
                if str(re_pic1).find("photo-item") != -1:
                    re_append_pic2 = re.findall('src="(.*?)"', str(re_pic1), re.S)
                    re_append_pic1 = str(re_append_pic2).replace("['", "")
                    re_append_pic = str(re_append_pic1).replace("']", "")
                else:
                    re_append_pic = ""

                re_video1 = re.findall('class="tb-rev-item-media"(.*?)</div>', str(re_append), re.S)
                if str(re_video1).find("video-item") != -1:
                    re_append_video2 = re.findall('mp4-src="(.*?)"', str(re_video1), re.S)
                    re_append_video1 = str(re_append_video2).replace("['", "")
                    re_append_video = str(re_append_video1).replace("']", "")
                else:
                    re_append_video = ""

                if str(re_append).find("[掌柜回复]") != -1:
                    re_reply1 = re.findall('[掌柜回复](.*?)<div', str(re_append), re.S)
                    re_reply2 = re.findall('</span>(.*?)</div>', str(re_reply1), re.S)
                    re_reply3 = str(re_reply2).replace("['", "")
                    re_reply = str(re_reply3).replace("']", "")
                else:
                    re_reply=""

                if str(re_append).find("[追加评论]") != -1:
                    re_zp1 = re.findall('[追加评论](.*?)<div', str(re_append), re.S)
                    re_zp2 = re.findall('</span>(.*?)</div>', str(re_zp1), re.S)
                    re_zp3 = str(re_zp2).replace("['", "")
                    re_zp = str(re_zp3).replace("']", "")
                else:
                    re_zp=""
            else:
                re_append_pic = ""
                re_append_video = ""
                re_reply = ""
                re_zp = ""

            str_temp1 = re.findall('class="tb-r-info"(.*?)div>', str(tmp_str[i]), re.S)
            re_time2 = re.findall('class="tb-r-date">(.*?)</span>', str(str_temp1), re.S)
            re_time3 = str(re_time2).replace("['", "")
            re_time = str(re_time3).replace("']", "")

            re_pro2 = re.findall('</span>(.*?)</', str(str_temp1), re.S)
            re_pro1 = str(re_pro2).replace("['", "")
            re_pro = str(re_pro1).replace("']", "")

            if str(tmp_str[i]).find("tb-r-action-btn") != -1:
                re_useful_num1 = re.findall('class="tb-r-action-btn"(.*?)</span>', str(tmp_str[i]), re.S)
                re_useful_num2 = re.findall('title="(.*?)"', str(re_useful_num1), re.S)
                re_useful_num3 = str(re_useful_num2).replace("有", "")
                re_useful_num4 = str(re_useful_num3).replace("人认为此评论用", "")
                re_useful_num5 = str(re_useful_num4).replace("['", "")
                re_useful_num = str(re_useful_num5).replace("']", "")
            else:
                re_useful_num=""
            tb_num3=tb_num2 + i + 1
            time.sleep(2)

            tb_num3 = escape_string(str(tb_num3))
            url = escape_string(str(url))
            cus_id = escape_string(str(cus_id))
            cus_name = escape_string(str(cus_name))
            cus_rank = escape_string(str(cus_rank))
            re_content = escape_string(str(re_content))
            re_pic = escape_string(str(re_pic))
            re_video = escape_string(str(re_video))
            re_append_pic = escape_string(str(re_append_pic))
            re_append_video = escape_string(str(re_append_video))
            re_reply = escape_string(str(re_reply))
            re_zp = escape_string(str(re_zp))
            re_time = escape_string(str(re_time))
            re_pro = escape_string(str(re_pro))
            re_useful_num = escape_string(str(re_useful_num))

            # 保存内容
            sql = "insert into review values (\'%s\'"
            for i in range(14):
                sql += ",\'%s\'"
            sql += ")"
            cur.execute(sql % (tb_num3,url,cus_id, cus_name, cus_rank, re_content, re_pic, re_video,re_append_pic,re_append_video,re_reply,re_zp,re_time,re_pro,re_useful_num))
            print(str("第"+str(tb_num3)+"条评论信息存储成功！"))

        tb_num2 = int(tb_num3)
        if str(html).find("pg-next") != -1 & str(html).find("pg-next pg-disabled") == -1:
            str_tbclick2 = browser.find_element_by_css_selector("#reviews > div > div > div > div > div > div.tb-revbd > div > ul > li.pg-next")
            str_tbclick2.click()
            time.sleep(10)
        else:
            if str(html).find("pg-next pg-disabled") != -1 or str(html).find("pg-next") == -1:
                break
    return(tb_num)

if __name__ == "__main__":
    readPath = open('TaobaoCookies.pickle', 'rb')
    tbCookies = pickle.load(readPath)
    with open('url.csv', 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    a=0
    for a in range(int(len(result))):
        # 连接MYSQL数据库
        db = pymysql.connect(host='127.0.0.1', user='root', password='Huang2419', db='taobao', port=3306, charset='utf8mb4')
        print('连接数据库成功！')
        cur = db.cursor()  # 获取指针以操作数据库
        uid = result[a]
        uid1 = str(uid).replace("[\'", "")
        uid2 = str(uid1).replace("\']", "")
        url = uid2
        browser.get(url)
        for cookie in tbCookies:
            browser.add_cookie({
                "domain": ".taobao.com",
                "name": cookie,
                "value": tbCookies[cookie],
                "path": '/',
                "expires": None
            })
        time.sleep(1)
        browser.get(url)
        html = browser.page_source
        if str(html).find("您查看的宝贝不存在") != -1:
            with open('output.csv', 'a', encoding='utf-8') as infofile:
                infofile.write("该产品已下架:" + str(url) + '\n')
                infofile.flush()
                infofile.close()
                time.sleep(0.2)
            print("该产品已下架")
        else:
            if str(html).find("我的淘宝") == -1&str(html).find("购物车") == -1:
                with open('output.csv', 'a', encoding='utf-8') as infofile:
                    infofile.write("该网页不是淘宝网页:" + str(url) + '\n')
                    infofile.flush()
                    infofile.close()
                    time.sleep(0.2)
                print("该网页不是淘宝网页")
            else:
                pro_review_num2 = re.findall('J_RateCounter">(.*?)</strong>', str(html), re.S)
                pro_review_num1 = str(pro_review_num2).replace("['", "")
                pro_review_num = str(pro_review_num1).replace("']", "")
                if pro_review_num == "[]":
                    pro_review_num = 0
                else:
                    pro_review_num = pro_review_num
                if int(pro_review_num) == 0:
                    get_tbshop()
                    get_tbproduct()
                    db.commit()
                    db.close()
                    print("数据存储成功")
                else:
                    get_tbshop()
                    get_tbproduct()
                    tb_num = get_tbreview()
                    html = browser.page_source
                    if int(tb_num) == 0:
                        print("网络连接存在问题，需稍后再试")
                    else:
                        if str(html).find("请按住滑块") != -1:
                            print("爬取过于频繁，需稍后再试")
                        else:
                            db.commit()
                            db.close()
                            print("数据存储成功")
        time.sleep(15)

