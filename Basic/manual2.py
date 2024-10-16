from sklearn.datasets import load_iris
iris = load_iris ()
print(iris.feature_names)






X = iris.data[:, :4]
y = iris.target
from sklearn.model_selection import train_test_split
X_train ,X_test ,y_train ,y_test=train_test_split(X,y,test_size =0.30)



from sklearn.preprocessing import StandardScaler
scaler = StandardScaler ()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


print(X_train.shape)
print(X_test.shape)


print(y_train.shape)
print(y_test.shape)


from sklearn.neighbors import KNeighborsClassifier

from sklearn import metrics

range_k = range(1,15)
scores = {}
scores_list = []
for k in range_k:
classifier = KNeighborsClassifier(n_neighbors=k)
classifier.fit(X_train , y_train)
y_pred = classifier.predict(X_test)
scores[k] = metrics.accuracy_score(y_test ,y_pred)
scores_list.append(metrics.accuracy_score(y_test ,y_pred))
result = metrics.confusion_matrix(y_test , y_pred)
print("Confusion Matrix:")
print(result)
result1 = metrics.classification_report(y_test , y_pred)
print("Classification Report:",)
print (result1)

%matplotlib inline
import matplotlib.pyplot as plt
plt.plot(range_k ,scores_list)
plt.xlabel("Value of K")
plt.ylabel("Accuracy")



classes = {0:'setosa',1:'versicolor',2:'virginicia'}
x_new = [[1,1,1,1],[4,3,1.3,0.2]]
y_predict = classifier.predict(x_new)
print(classes[y_predict [0]])
print(classes[y_predict [1]])