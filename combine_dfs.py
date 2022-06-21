import os
import sys

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

data_path = ' '.join(sys.argv[1:]) # enter dataset path from command line

target_df = pd.read_csv(os.path.join(data_path, 'dataset', 'MovementAAL_target.csv'))

labels = target_df[' class_label']
labels.rename('class_label', inplace=True) # remove the leading whitespace

X_train = pd.DataFrame()
X_test = pd.DataFrame()

sequence_ids = target_df['#sequence_ID']

train_ids, test_ids, train_labels, test_labels = train_test_split(sequence_ids, labels, test_size=0.2)

for sequence in train_ids:
    df = pd.read_csv(os.path.join(data_path, 'dataset', f'MovementAAL_RSS_{sequence}.csv'))
    df.insert(0, 'sequence', sequence-1)
    df['step'] = np.arange(df.shape[0])
    X_train = pd.concat([X_train, df])

for sequence in test_ids:
    df = pd.read_csv(os.path.join(data_path, 'dataset', f'MovementAAL_RSS_{sequence}.csv'))
    df.insert(0, 'sequence', sequence-1)
    df['step'] = np.arange(df.shape[0])
    X_test = pd.concat([X_test, df])

X_train.to_csv('train.csv', index=False)
X_test.to_csv('test.csv', index=False)

train_labels.to_csv('train_labels.csv', index=False)
test_labels.to_csv('test_labels.csv', index=False)