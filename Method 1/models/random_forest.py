from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

train_labels = pd.read_csv('../../train_labels.csv')
test_labels = pd.read_csv('../../test_labels.csv')

train_features = pd.read_csv('../train_features.csv')
test_features = pd.read_csv('../test_features.csv')

rf = RandomForestClassifier(n_estimators = 1000)
rf.fit(train_features, train_labels['class_label'])


print(accuracy_score(test_labels['class_label'], rf.predict(test_features)))
