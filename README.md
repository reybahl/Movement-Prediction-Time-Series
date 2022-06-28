# Dataset

In this project, time series classification is used to predict the pattern of user movements in real-world office environments. 

This problem involves determining whether or not an individual has moved between rooms based on time series of radio signal strength (RSS) between nodes of a Wireless Sensor Network (WSN).

The dataset was collected and made available by researchers from the University of Pisa in Italy. It is described in their paper [An experimental characterization of reservoir computing in ambient assisted living applications](https://link.springer.com/article/10.1007/s00521-013-1364-4).

## Downloading the dataset

The dataset can be found in the UCI Machine Learning Repository using this [link](https://archive.ics.uci.edu/ml/datasets/Indoor+User+Movement+Prediction+from+RSS+data).

# How to run the code
Install the required libraries using the following command:

`pip install -r requirements.txt`

Run `combine_dfs.py` to aggregate all the time series samples. This program takes command-line input for the dataset directory. For example, if the relative path to the dataset is `Dataset`, run the program using the following command:

`python combine_dfs.py Dataset`.

This splits the data into training and testing data and generates 4 files:
* `train.csv` - contains the training time series samples
* `test.csv` - contains the testing time series samples
* `train_labels.csv` - contains the classification of each sample in train.csv
* `test_labels.csv` - contains the classification of each sample in test.csv
