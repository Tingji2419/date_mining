# python
# -*- encoding: utf-8 -*-

import numpy as np
import gensim
from sklearn.cluster import KMeans
import matplotlib
import matplotlib.pyplot as pl

model = gensim.models.word2vec.Word2Vec.load('data.model')

#
# def predict_proba(oword, iword):
#     iword_vec = model.wv.get_vector(iword, norm=True)
#     oword = model.wv.get_vector(oword)
#
#     #oword_l = model.syn1[oword.point].T
#     oword_l = oword
#     dot = np.dot(iword_vec, oword_l)
#     lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot)
#     return lprob
#
#
# def keywords(s):
#     s = [word for word in s if word in model.wv]
#     ws = {word: sum([predict_proba(u, word) for u in s]) for word in s}
#     return Counter(ws).most_common()

if __name__ == "__main__":
    f = open('data_result.txt', 'r', encoding='utf-8')
    w = open('final_result.txt', 'w', encoding='utf-8')

    keys = model.wv
    wordvector = []
    for key in keys.vectors:
        wordvector.append(key)

    # 分类
    clf = KMeans(n_clusters=10)
    s = clf.fit(wordvector)
    print(s)
    # 获取到所有词向量所属类别
    labels = clf.labels_

    # 获取聚类中心
    cent = clf.cluster_centers_
    centroids = []
    for i in range(0, 10):
        min = 99999
        flag = 0
        for j in range(0, len(wordvector)):
            if min > np.linalg.norm(cent[i] - wordvector[j]):
                min = np.linalg.norm(cent[i] - wordvector[j])
                flag = j
        centroids.append(keys.index_to_key[flag])

    class_distance_count = [0]*10
    for i in range(0, len(wordvector)):
        temp = np.linalg.norm(cent[labels[i]] - wordvector[i])
        class_distance_count[labels[i]] = class_distance_count[labels[i]] + temp
    with open('output/聚类中心.txt', 'w') as f:
        for i in centroids:
            f.write(str(i))
            f.write('\t')

    # 把是一类的放入到一个集合
    classCollects = {}
    for i in range(len(keys)):
        if labels[i] in classCollects.keys():
            classCollects[labels[i]].append(keys[i])
        else:
            classCollects[labels[i]] = [keys[i]]

    # 画图
    x = []
    y = []
    for i in range(0, 9):
        x.append(centroids[i])
        y.append(len(classCollects[i])/class_distance_count[i])
    matplotlib.rcParams['font.family'] = 'SimHei'   # 中文显示
    fig, ax = pl.subplots()
    ax.bar(x, y, width=0.5)
    ax.set_xlabel("关键词")  # 设置x轴标签
    ax.set_ylabel("聚类指标")  # 设置y轴标签
    ax.set_title("用户关注点")  # 设置标题
    # 添加x坐标对应的label
    # pl.xticks([i + 1 for i in range(19)], x, rotation=90)
    pl.show()  # 显示图像
    print()
