import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

train_labels = pd.read_csv('../../train_labels.csv')
test_labels = pd.read_csv('../../test_labels.csv')

train_features = pd.read_csv('../train_features.csv')
test_features = pd.read_csv('../test_features.csv')

lr = LogisticRegression()
lr.fit(train_features, train_labels['class_label'])


print(accuracy_score(test_labels['class_label'], lr.predict(test_features)))
