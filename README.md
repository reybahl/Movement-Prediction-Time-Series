# Dataset

In this project, time series classification is used to predict the pattern of user movements in real-world office environments. 

This problem involves determining whether or not an individual has moved between rooms based on time series of radio signal strength (RSS) between nodes of a Wireless Sensor Network (WSN).

The dataset was collected and made available by researchers from the University of Pisa in Italy. It is described in their paper [An experimental characterization of reservoir computing in ambient assisted living applications](https://link.springer.com/article/10.1007/s00521-013-1364-4).

## Downloading the dataset

The dataset can be found in the UCI Machine Learning Repository using this [link](https://archive.ics.uci.edu/ml/datasets/Indoor+User+Movement+Prediction+from+RSS+data).

## Dataset structure
For this task, the `dataset` directory contains all the necessary data. The files are organized as below:

```
Dataset (can be named anything you want ... specify THIS directory when running combine_dfs.py)
    dataset
        MovementAAL_RSS_1.csv
        MovementAAL_RSS_2.csv
        ...
        MovementAAL_target.csv
```

Each of the `MovementAAL_RSS_{id}` files represents a time series with measurements in chronological order and contains four columns representing the RSS measurements.

`MovementAAL_target.csv` contains the label for each of these time series. The target class 1 represents location changing movements, while -1 reprents location preserving movements. 

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

After running the program, this is how the files will be organized:

```
Dataset
    dataset
        MovementAAL_RSS_1.csv
        MovementAAL_RSS_2.csv
        ...
        MovementAAL_target.csv
        
Method 1
    ... code for method 1

train_labels.csv
train.csv
test_labels.csv
test.csv
...
```
