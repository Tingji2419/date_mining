# python
# -*- coding: utf-8 -*-

import jieba.analyse
import codecs

# temp = pd.read_csv('服装品类.csv', usecols=[1], encoding='gbk')
# temp.to_csv('data1.txt', index=False, header=None, encoding='utf8')

f = codecs.open('data1.txt', 'r', encoding='utf8')
target = codecs.open('data_seg.txt', 'w', encoding='utf8')
stopkey = [w.strip() for w in codecs.open('stop_word.txt', 'r', encoding='utf-8').readlines()]
print("open files")
#count = 0
lineNum = 1
line = f.readline()
while line:
    print("---processiong", lineNum, "article---")
    seg_list = jieba.cut(line, cut_all = False)
    line_seg = ''
    for word in seg_list:
        if word not in stopkey:
           line_seg += word
           line_seg += ' '
    #line_seg = ' '.join(seg_list)
    target.writelines(line_seg)
    lineNum += 1
    line = f.readline()
 
print("well done")
f.close()
target.close()