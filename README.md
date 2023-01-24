# Intrusion-Detection

An Intrusion Detection Application that detects which type of attacks that happens on a network

## Run the app

```Powershell
# conda terminal
streamlit run app.py

#Application

 https://genga-intrusion-detection.streamlit.app/

```


## Dataset Description

Features -- 41
Rows -- 1,48,519

Test data -- 22,545 rows
Train data -- 1,25,974 rows

Here in this project the dataset is loaded in three different ways:

    *Using Database -- MongoDB
    *As a txt file
    *As a csv file

## Models Used:

**Navie Bayes
    
    Model Accuracy -- 97.3%
    
    
    For 0:                           
    Precision -- 98%
    Recall -- 97%
    f1 score -- 97%
    For 1:                           
    Precision -- 97%
    Recall -- 98%
    f1 score -- 97%

**Decision Tree(ID3)
    
    Model Accuracy -- 99.9%
    
    For 0 and 1:
    Precision -- 100%
    Recall -- 100%
    f1 score -- 100%

**KNN
    
    Model Accuracy -- 99.7%
    
    For 0 and 1:
    Precision -- 100%
    Recall -- 100%
    f1 score -- 100%
    
**Logistic Regression
    
    Model Accuracy -- 98%
    
    For 0:                           
    Precision -- 99%
    Recall -- 97%
    f1 score -- 98%
    For 1:                           
    Precision -- 97%
    Recall -- 99%
    f1 score -- 98%

Hence ID3 is chosen for prediction

## Screenshot

![image](https://user-images.githubusercontent.com/82211151/213107450-a4aaa8ec-59a3-4a0c-b3d9-8ef115f42398.png)

![image](https://user-images.githubusercontent.com/82211151/213107515-05567f66-22c5-4cf7-beff-03f3adec0388.png)





