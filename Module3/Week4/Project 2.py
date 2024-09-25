import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
import math

# Bài tập 1
df = pd.read_csv('D:/Homework/Module3/Week4/cleveland.csv', header = None)
df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol',
              'fbs', 'restecg', 'thalach', 'exang',
              'oldpeak', 'slope', 'ca', 'thal', 'target']
df['target'] = df.target.map({0: 0, 1: 1, 2: 1, 3: 1, 4: 1})
df['thal'] = df.thal.fillna(df.thal.mean())
df['ca'] = df.ca.fillna(df.ca.mean())

# distribution of target vs age
# sns.set_context("paper", font_scale = 1, rc = {"font.size":3, 'axes.titlesize':10})
# ax = sns.catplot(kind = 'count', data = df, x = 'age', hue = 'target', order = df['age'].sort_values().unique())
# ax.ax.set_xticks(np.arange(0, 80, 5))
# plt.show()

#bai tap 2
# sns.catplot(kind = 'bar', data = df, y = 'age', x = 'sex', hue = 'target')
# plt.show()
X = df.iloc[:,:-1]
y = df.iloc[:, -1]
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

### KNN

from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier(n_neighbors = 5, weights = 'uniform', algorithm = 'auto', leaf_size = 30, p =2, metric = 'minkowski')
KNN.fit(X_train, y_train)
y_pred = KNN.predict(X_test)
y_train_pred = KNN.predict(X_train)
print(accuracy_score(y_pred, y_test))
print(accuracy_score(y_train_pred,y_train))

### Naive_bayes

from sklearn.naive_bayes import GaussianNB
naive_bayess = GaussianNB()
naive_bayess.fit(X_train, y_train)
y_pred = naive_bayess.predict(X_test)
y_train_pred = naive_bayess.predict(X_train)
print(accuracy_score(y_pred, y_test))
print(accuracy_score(y_train_pred,y_train))

### Decisiontree

from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier(criterion = 'gini', max_depth=10, min_samples_split = 2, random_state = 42)
DT.fit(X_train, y_train)
y_pred = DT.predict(X_test)
y_train_pred = DT.predict(X_train)
print(accuracy_score(y_pred, y_test))
print(accuracy_score(y_train_pred,y_train))

### RandomForest

from sklearn.ensemble import RandomForestClassifier
RF = RandomForestClassifier(criterion = 'gini', max_depth=10, min_samples_split = 2, n_estimators = 10, random_state = 42)
RF.fit(X_train, y_train)
y_pred = RF.predict(X_test)
y_train_pred = RF.predict(X_train)
print(accuracy_score(y_pred, y_test))
print(accuracy_score(y_train_pred,y_train))

### AdaBoost

from sklearn.ensemble import AdaBoostClassifier
ADB = AdaBoostClassifier(learning_rate= 1.0, n_estimators = 10, random_state = 42)
ADB.fit(X_train, y_train)
y_pred = ADB.predict(X_test)
y_train_pred = ADB.predict(X_train)
print(accuracy_score(y_pred, y_test))
print(accuracy_score(y_train_pred,y_train))

### Gradiant boosting

from sklearn.ensemble import GradientBoostingClassifier
GB = GradientBoostingClassifier(learning_rate= 0.1, n_estimators = 100, subsample = 1.0, min_samples_split = 2, max_depth = 3, random_state = 42)
GB.fit(X_train, y_train)
y_pred = GB.predict(X_test)
y_train_pred = GB.predict(X_train)
print(accuracy_score(y_pred, y_test))
print(accuracy_score(y_train_pred,y_train))

### XGboost

from xgboost import XGBClassifier
XGB = XGBClassifier(objective= "binary:logistic", random_state = 42, n_estimators = 100)
XGB.fit(X_train, y_train)
y_pred = XGB.predict(X_test)
y_train_pred = XGB.predict(X_train)
print(accuracy_score(y_pred, y_test))
print(accuracy_score(y_train_pred,y_train))