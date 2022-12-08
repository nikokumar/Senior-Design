import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from ta.utils import dropna
from ta.momentum import RSIIndicator
from ta.trend import macd, EMAIndicator
from sklearn.model_selection import train_test_split
import datetime as dt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

yf.pdr_override()
data = pdr.get_data_yahoo("TXN")
#data = data.iloc[10000:]

#Use this when we randomly drop columns for fine tuning
#data = add_all_ta_features(data, open="Open", high="High", low="Low", close="Close", volume="Volume")



indicator_macd = macd(close=data["Adj Close"], fillna=True)
indicator_ema = EMAIndicator(close=data["Adj Close"], fillna=True)
indicator_rsi = RSIIndicator(close=data["Adj Close"], window= 14, fillna=True)

data['macd'] = indicator_macd
data['ema'] = indicator_ema.ema_indicator()
data['rsi'] = indicator_rsi.rsi() 

#print(data)
data = dropna(data)
#print(data)

X_train, X_test, y_train, y_test = train_test_split(data[['Adj Close']], data[['ema']], test_size=.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)



print("Model Coefficients:", model.coef_)
print("Root Mean Square Error:", mean_squared_error(y_test,y_pred, squared=False))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Coefficient of Determination:", r2_score(y_test, y_pred))

