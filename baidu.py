from lxml import etree
#使用Selenium模拟百度搜索
from selenium import webdriver
import time

# 一、声明浏览器对象：使用谷歌驱动
#chrome选项,一些浏览器设置
#使用无头chrome，不跳出窗口
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
                          , options = options)

# 二、调用该浏览器对象driver，让其执行各个模拟浏览器的操作

#1、访问页面，参数传入URL即可
driver.get("https://www.baidu.com")
#由于有可能存在网络加载慢等原因，所以这里先加载时暂停2秒
# （这个暂停时间具体根据实际情况设置）之后再去获取表单元素
time.sleep(2)

#2、查找元素节点：为完成搜索操作，需要定位到搜索框
#常用方法：(1)find_element_by_id()、find_element_by_name()、……
#(2)find_element_by_xpath()、find_element_by_css_selector()、……
#(3)通用方法find_elements()
# 输入框、按钮
kw=driver.find_element_by_id("kw")
su=driver.find_element_by_id("su")

#3、向定位到的元素进行操作：输入查询条件并提交
# （1）input填入值
kw.send_keys("Python")
#（2）点击提交
su.click()
# 其他常用操作，清空文字clear()、鼠标拖拽（动作链）、下拉进度条
time.sleep(2)

# 三、已进入页面，解析页面获得目标内容
content = driver.page_source  # HTML内容
#contentx = etree.HTML(content)  # lxml解析
#c = contentx.xpath('……') #获取目标内容

# 四、关闭浏览器
driver.close()