from sklearn import svm

X = [[-4,-4,-1],[-2,-2,0],[1,1,2],[3,3,5]]
y = [1,1,0,0]
clf = svm.SVC(kernel='rbf')
clf.fit(X, y)
a = [2,2,4]
ans = clf.predict([a])

print ans
