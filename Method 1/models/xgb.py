import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

train_labels = pd.read_csv('../../train_labels.csv')
test_labels = pd.read_csv('../../test_labels.csv')

train_features = pd.read_csv('../train_features.csv')
test_features = pd.read_csv('../test_features.csv')

train_X, val_X, train_y, val_y = train_test_split(train_features, train_labels) 

xgb_model = XGBClassifier(n_estimators=2000, learning_rate=0.01, objective= 'binary:logistic')
xgb_model.fit(train_X, train_y, early_stopping_rounds=2000, eval_set=[(val_X, val_y)])

print(accuracy_score(test_labels['class_label'], xgb_model.predict(test_features)))
