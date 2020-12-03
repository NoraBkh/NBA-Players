# Binary classification of NBA Players


## Introduction

This is a binary classification project that aims to predict whether a NBA player's career will last for more than 5 years or not. The data includes the performance metrics of NBA players, using which the predictions have to be made.

Once the classifier has been trained, it is integrated as a webservice using Flask. This web service in REST API format take as input all the relevant parameters that have been identified as if it were made available to a user wishing to make a single player request to the trained model.
## Installation


```bash
sudo apt-get install python python-pip
sudo apt-get install python3-flask
sudo pip install flask
```

## Data

The dataset contains columns giving values for points attained by NBA players in their careers. The description of column names is given in a file named Column Name Explanations.png file (image file), which is present in the repository.

The dataset is also present in the repository in a CSV file format.

## Requirements

The project was done in Jupyter Notebook, Python 3.