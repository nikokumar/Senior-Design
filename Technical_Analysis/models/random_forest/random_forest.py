# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xg1NQzuYQb9DWQ4tssksoECez6CHlD5I
"""

#!pip install yfinance

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from pandas_datareader import data as pdr
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

class Random_Forest_Regressor:
    def __init__(self):
        #Needs input of which variables so can be expanded to uni/multivariate maybe list of feature names to get from data
        yf.pdr_override()
        self.stock_data = pdr.get_data_yahoo("TXN") #consider saving somewhere and not downloading every time and to include which features from  list
        self.stock_data = self.stock_data.iloc[12000:]
        self.supervised_data = self.create_supervised_data()

    def evaluate(self, n_test): #needs batch size and num features
        predictions = list()
        
        train, test = self.train_test_split(self.supervised_data, n_test) #can be a better call
        history = [x for x in train]

        for i in range(len(test)):
            testX, testy = test[i, :-1], test[i, -1]
            pred = self.forecast(history, testX)
            predictions.append(pred)
            history.append(test[i])
        
       

        return predictions, test[:, -1]

    def forecast(self, train, testX):
        train = np.asarray(train)
        trainX, trainy = train[:, :-1], train[:, -1]

        model = RandomForestRegressor(n_estimators=200) #must tune hyperparameters
        model.fit(trainX, trainy)

        #make a single prediciton
        pred = model.predict(np.asarray([testX]))

        return pred[0]

    def train_test_split(self, data, n_test):
        return data[:-n_test, :], data[-n_test:, :] #does this work for multivariate

    def create_supervised_data(self, X_lag=63, y_lag=1):
        n_vars = 1 #Univariate
        #n_vars = 1 if type(data) is list else data.shape[1] # Use this when making multivariate able

        df = self.stock_data['Adj Close'].copy() #this will need to change for multivariate
        cols, names = list(), list()
	    # input sequence (t-n, ... t-1)
        for i in range(X_lag, 0, -1):
            cols.append(df.shift(i))
            names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)] #Change this to better name the features

        # forecast sequence (t, t+1, ... t+n)
        for i in range(0, y_lag):
            cols.append(df.shift(-i))
            if i == 0:
                names += [('var%d(t)' % (j+1)) for j in range(n_vars)] # change this to name Adj Close or similar
            else:
                names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)] # change this to name Adj Close or similar

        agg = pd.concat(cols, axis=1)
        agg.columns = names
        agg.dropna(inplace=True) # may need a variable for dropna if some indicators have several na features
        return agg.values

    # ticker = "txn"
    # stock_data = yf.download(ticker, start="2010-01-04", end="2021-05-12")
    # stock_data = pd.DataFrame(stock_data)
    # stock_data.dropna(inplace=True)
    # stock_data.describe()

    # y = stock_data['Adj Close']
    # X = stock_data.drop('Adj Close', axis = 1)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    # #print(len(X_train))
    # #print(len(y_train))

    # rf = RandomForestRegressor(n_estimators=200)
    # rf.fit(X_train, y_train)
    # y_test_pred = rf.predict(X_test)
    # rfr_mse = mean_squared_error(y_test, y_test_pred, squared = False)

    # data = [['Random Forest Regressor', rfr_mse]]
    # df = pd.DataFrame(data, columns=['Model', 'RMSE'])
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.precision', 4):
    #     print(df)