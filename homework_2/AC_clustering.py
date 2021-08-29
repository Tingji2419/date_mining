import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering as AC
from sklearn.decomposition import PCA

tfidf = pd.read_csv('tfidf.csv')
data = tfidf.values[:, 1:]

numClass = 4
AC_model = AC(n_clusters=numClass, affinity="euclidean", linkage='ward')   # 层次聚类
pca = PCA(n_components=10)
TnewData = pca.fit_transform(data)  # 先降维
t0 = time.time()
AC_model.fit(TnewData)   # 再聚类
elapsed_time = time.time() - t0

pca = PCA(n_components=2)  # 为了画二维图，这里设置输出两维
newData = pca.fit_transform(data)  # 载入N维
result = AC_model.labels_   # labels_为聚类结果
plt.scatter(newData[:, 0], newData[:, 1], c=result, cmap=plt.cm.nipy_spectral)
plt.show()
print("time(s):", elapsed_time)
