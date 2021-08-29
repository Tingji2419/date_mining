
import os
import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
chrome_options.add_experimental_option('prefs', prefs)

#MAC版本
#browser = webdriver.Chrome(chrome_options=chrome_options)

#Windows版本
chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  #修改webdriver的绝对位置
browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

wait = WebDriverWait(browser, 10)
browser.implicitly_wait(1800)

def getTaobaoCookies():
    url = "https://www.taobao.com/"
    browser.get("https://login.taobao.com/member/login.jhtml")
    html = browser.page_source
    if str(html).find("扫码登录更安全") != -1:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#login > div.corner-icon-view.view-type-qrcode > i")))
        element.click()
    time.sleep(7)
    while True:
        time.sleep(3)
        html = browser.page_source
        if str(html).find("手机扫码，安全登录") != -1:
            time.sleep(20)
            html = browser.page_source
            if str(html).find("主题市场") == -1:
                browser.get("https://www.taobao.com/")
        else:
            if str(html).find("主题市场") == -1:
                browser.get("https://www.taobao.com/")
        while browser.current_url == url:
            tbCookies = browser.get_cookies()
            # print(tbCookies)
            # browser.quit() #此处应删去
            cookies = {}
            for item in tbCookies:
                cookies[item['name']] = item['value']
            outputPath = open('TaobaoCookies.pickle', 'wb')
            pickle.dump(cookies, outputPath)
            outputPath.close()
            return cookies


def readTaobaoCookies():
    if os.path.exists('TaobaoCookies.pickle'):
        readPath = open('TaobaoCookies.pickle', 'rb')
        tbCookies = pickle.load(readPath)
    else:
        tbCookies = getTaobaoCookies()
    return tbCookies


if __name__ == "__main__":
    tbCookies = readTaobaoCookies()
    browser.get("https://www.taobao.com/")
    for cookie in tbCookies:
        browser.add_cookie({
        "domain":".taobao.com",
        "name":cookie,
        "value":tbCookies[cookie],
        "path":'/',
        "expires":None
    })
    browser.get("https://www.taobao.com/")
