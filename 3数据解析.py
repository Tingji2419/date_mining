# from lxml import etree    # 导入etree子模块
# # 定义html字符串
# html_str = '''
# <div class="level_one on">
# <ul>
# <li>
#     <a href="/index/index/view/id/1.html" title="什么是Java" class="on">什么是Java</a>
#     <a>Java</a>
# </li>
# <li> <a href="javascript:" onclick="login(0)" title="Java的版本">Java的版本</a> </li>
# <li> <a href="javascript:" onclick="login(0)" title="Java API文档">Java API文档</a> </li>
# </ul>
# </div>
# '''
# html = etree.HTML(html_str)    # 解析html字符串
# a_all = html.xpath('//li/a')   # 获取li节点中所有子节点a
# print('所有子节点a',a_all)    # 打印所有a节点
# print('获取指定a节点：',a_all[1])  # 打印指定a节点
# a_txt = etree.tostring(a_all[1],encoding = "utf-8")   # 转换字符串类型,并进行编码
# # 打印指定节点的HTML代码
# print('获取指定节点HTML代码：',a_txt.decode('utf-8'))

from bs4 import BeautifulSoup  # 导入BeautifulSoup库

# 创建模拟HTML代码的字符串
html_doc = """
<html>
<head>
    <title>关联获取演示</title>
    <meta charset="utf-8"/>
</head>
</html>
"""
# 创建一个BeautifulSoup对象，获取页面正文
soup = BeautifulSoup(html_doc, features="lxml")
print(soup.title.parent)                # 打印title节点的父节点内容
print(soup.title.parents)               # 打印title节点的父节点及以上内容的generator对象
for i in soup.title.parents:           # 循环遍历generator对象中的所有父节点及以上内容
    print(i.name)                       # 打印父节点及祖先节点名称