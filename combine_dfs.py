import os
import sys

import numpy as np
import pandas as pd

data_path = ' '.join(sys.argv[1:]) # enter dataset path from command line

target_df = pd.read_csv(os.path.join(data_path, 'dataset', 'MovementAAL_target.csv'))

labels = target_df[' class_label']
labels.rename('class_label', inplace=True) # remove the leading whitespace

main_df = pd.DataFrame()
sequence_ids = target_df['#sequence_ID']

for sequence in sequence_ids:
    df = pd.read_csv(os.path.join(data_path, 'dataset', f'MovementAAL_RSS_{sequence}.csv'))
    df.insert(0, 'sequence', sequence-1)
    df['step'] = np.arange(df.shape[0])
    main_df = pd.concat([main_df, df])

main_df.to_csv('data.csv', index=False)
labels.to_csv('labels.csv', index=False)