# coding: utf-8


import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

a=np.random.random((10,5))+2
b=np.random.random((10,5))+5
c=np.random.random((10,5))+8
X=np.concatenate((a,b,c))

p= pdist(X, metric="euclidean") #ユークリッド距離を採用する
Z= linkage(p, method="single") #最小最短距離法をmethodで指定する

dendrogram(Z)

plt.show()
