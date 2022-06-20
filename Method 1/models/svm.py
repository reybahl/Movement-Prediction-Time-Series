import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

train_labels = pd.read_csv('../../train_labels.csv')
test_labels = pd.read_csv('../../test_labels.csv')

train_features = pd.read_csv('../train_features.csv')
test_features = pd.read_csv('../test_features.csv')

svm = SVC(gamma='auto')
svm.fit(train_features, train_labels['class_label'])


print(accuracy_score(test_labels['class_label'], svm.predict(test_features)))
