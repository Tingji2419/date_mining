# -encoding-utf8
# 2021-8

import numpy as np
import pandas as pd
import re
from gensim import corpora, models, similarities
import gensim

df = pd.read_csv("data1.txt", error_bad_lines=False)


docslist = df.values
texts = [[word for word in str(doc).replace('[', '').replace(']', '').replace('\'', '').split()] for doc in docslist]


dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20)
# 将单个主题作为格式化字符串
# 返回：主题的字符串表示，如'-0.340 *“类别”+ 0.298 *“$ M $”+ 0.183 *“代数”+ ...“。
# topicno：主题ID，这里是10
# topn: 将使用的主题中的单词数
print(lda.print_topic(10, topn=5))

# lda.print_topics(num_topics=20, num_words=5)

print('end')
