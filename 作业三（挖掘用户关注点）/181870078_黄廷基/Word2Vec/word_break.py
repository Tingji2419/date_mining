# python
# -*- coding: utf8 -*-

import re
import codecs
import pandas as pd
import csv

# temp = pd.read_csv('stop_word.txt', sep='\t', quoting=csv.QUOTE_NONE)
# temp.to_csv('stop_word.txt', index=False, header=None, encoding='utf-8')

f = open("data_seg.txt", 'r', encoding='utf-8')
stopkey = [w.strip() for w in codecs.open('stop_word.txt', 'r', encoding='utf-8').readlines()]
w = open('data_result.txt', 'w', encoding='utf-8')
  
  
  
seg = f.readline()
while seg:
    l = []
    s1 = re.split(' ', seg)

    for i in s1:
        i = re.sub(r"[0-9]", "", i)
        i = re.sub(r"[a-zA-Z]", "", i)  # 英文，没意义
        i = re.sub(r"!", "", i)
        i = re.sub(r"/?", "", i)
        i = re.sub(r" ", "", i)
        i = re.sub(r"，", "", i)
        i = re.sub(r"  ", "", i)
        if i not in l and i not in stopkey:
            l.append(i)
            #allword.append(i)
    for j in l:
        w.write(j)
        w.write('   ')
    seg = f.readline()

f.close()
w.close()