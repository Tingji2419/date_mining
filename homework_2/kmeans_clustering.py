import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

tfidf = pd.read_csv('tfidf.csv')
data = tfidf.values[:, 1:]

# CV方法确定k值

# SSE = []  # 存放每次结果的误差平方和
# for k in range(1, 9):
#     estimator = KMeans(n_clusters=k)  # 构造聚类器
#     estimator.fit(data)
#     SSE.append(estimator.inertia_)
# X = range(1, 9)
# plt.xlabel('k')
# plt.ylabel('SSE')
# plt.plot(X, SSE, 'o-')
# plt.show()

numClass = 4
clf = KMeans(n_clusters=numClass, max_iter=1000, init="k-means++")    # Kmeans
pca = PCA(n_components=10)
TnewData = pca.fit_transform(data)  # 先降维
t0 = time.time()
s = clf.fit(TnewData)   # 再聚类
elapsed_time = time.time() - t0     # 运行时间

# 画图函数
def plot_cluster(result, newData, numClass):
    plt.figure(2)
    Lab = [[] for i in range(numClass)]
    index = 0
    for labi in result:
        Lab[labi].append(index)
        index += 1
    color = ['oy', 'ob', 'og', 'cs', 'ms', 'bs', 'ks', 'ys', 'yv', 'mv', 'bv', 'kv', 'gv', 'y^', 'm^', 'b^', 'k^',
             'g^'] * 3
    for i in range(numClass):
        x1 = []
        y1 = []
        for ind1 in newData[Lab[i]]:
            # print ind1
            try:
                y1.append(ind1[1])
                x1.append(ind1[0])
            except:
                pass
        plt.plot(x1, y1, color[i])

    # 绘制初始中心点
    x1 = []
    y1 = []
    for ind1 in clf.cluster_centers_:
        try:
            y1.append(ind1[1])
            x1.append(ind1[0])
        except:
            pass
    plt.plot(x1, y1, "rv")  # 绘制中心
    plt.show()


pca = PCA(n_components=2)  # 为了画二维图，这里设置输出两维
newData = pca.fit_transform(data)  # 载入N维
result = list(clf.predict(TnewData))    # 输出Kmeans聚类结果

output = pd.read_csv('清洗后的data.csv')
output['label'] = result
output.to_csv('output.csv')

plot_cluster(result, newData, numClass)
print("time(s):", elapsed_time)

