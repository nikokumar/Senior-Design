import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from ta.utils import dropna
from ta.momentum import RSIIndicator
from ta.trend import macd, EMAIndicator

def update_txn_csv(only_history=False, X_lag=63):
    yf.pdr_override()
    stock_data = pdr.get_data_yahoo("TXN", "2010-01-04") #consider saving somewhere and not downloading every time and to include which features from  list
    #stock_data = stock_data.iloc[12000:]
    #print(stock_data)
    #stock_data = stock_data['Adj Close'].copy()
    
    data = pd.DataFrame(columns=['Adj Close'])
    data['Adj Close'] = stock_data['Adj Close'].copy()
    
    #print(data)

    csv_path = 'Technical_Analysis/data/'
    csv_name = 'supervised_{}_days_history.csv'.format(X_lag)
    if not only_history:
        indicator_macd = macd(close=data['Adj Close'], fillna=True)
        #indicator_ema = EMAIndicator(close=stock_data, fillna=True)
        indicator_rsi = RSIIndicator(close=data['Adj Close'], window= 14, fillna=True)

        data['macd'] = indicator_macd
        #stock_data['ema'] = indicator_ema.ema_indicator()
        data['rsi'] = indicator_rsi.rsi() 
        csv_name = 'supervised_{}_days_indicators.csv'.format(X_lag)
    #print(stock_data)
    #print(type(stock_data))
    supervised_data = create_supervised_data(data, X_lag)
    df = pd.DataFrame(supervised_data)
    df.to_csv(csv_path+csv_name)

def create_supervised_data(stock_data, X_lag=63, y_lag=1):
        #n_vars = 1 #Univariate
        n_vars = 1 if type(stock_data) is list else stock_data.shape[1] # Use this when making multivariate able

        df = pd.DataFrame(stock_data) #this will need to change for multivariate
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

