from selenium import webdriver
import time
#使用谷歌驱动
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#使用Selenium模拟百度搜索
#打开登录页面
driver.get("https://www.baidu.com")
#由于有可能存在网络加载慢等原因，所以这里先加载时暂停2秒
# （这个暂停时间具体根据实际情况设置）之后再去获取表单元素
time.sleep(2)
#定位到搜索框
kw=driver.find_element_by_id("kw")
#向定位到的input填入值
kw.send_keys("Python")
#定位su提交按钮
su=driver.find_element_by_id("su")
#模拟点击提交
su.click()
