from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
import pandas as pd
data = pd.read_csv('mod_comps.csv', names = ["C1", "C2", "C3", "C4", "C5", "C6", "C7","gpsqi","score"])
print("\nDescription of the data:\n",(data.describe()).transpose())
#print(len(data.loc[0:,]))
#data = pd.read_csv('comps.csv')
x=data.drop('gpsqi', axis=1)
x=data.drop('score',axis=1)
y=data['score']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.35)
scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
#print(x_test)
x_test = scaler.transform(x_test)
#print(x_test[0])
mlp = MLPClassifier(hidden_layer_sizes=(7,7,7),max_iter=1000)
mlp.fit(x_train,y_train)
#p=mlp.predict(x_test)
predictions = mlp.predict(x_test)
print("\nConfusion Matrix:\n",confusion_matrix(y_test,predictions))
print("\nClassification Report:\n",classification_report(y_test,predictions))
#print(predictions)
y=list(y_test)
#print(y, sep=' ')
correct=0
actual = list(predictions)
for i in range(len(predictions)):
	if y[i] == predictions[i]:
		correct += 1
acc=correct / float(len(actual)) * 100.0
print(acc)
