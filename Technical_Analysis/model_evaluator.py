from sklearn.metrics import mean_squared_error
from data_collector import update_txn_csv
from models.XGBoost import XGB_univariate
from models.XGBoost import XGB_multi
from models.random_forest import random_forest
import pandas as pd
import matplotlib.pyplot as plt

'''

Suggestions:
 - Search through all models folders and compare all models
 - Input list of models to test
'''
update_txn_csv()

xgb_uni = XGB_univariate.XGB_Univariate()
rf = random_forest.Random_Forest_Regressor()
xgb_multi = XGB_multi.XGB_multi()

xgb_univariate_pred, xgb_univariate_actual = xgb_uni.evaluate(10)
xgb_univariate_mse = mean_squared_error(xgb_univariate_actual, xgb_univariate_pred, squared=False)

xgb_multi_pred, xgb_multi_actual = xgb_multi.evaluate(10)
xgb_multi_mse = mean_squared_error(xgb_multi_actual, xgb_multi_pred, squared=False)

rf_pred, rf_actual = rf.evaluate(10)
rf_mse = mean_squared_error(rf_actual, rf_pred, squared=False)

data = [['XGB_univariate', xgb_univariate_mse],['Random_Forest_Regressor',rf_mse],['XGB_multivariate',xgb_multi_mse]]
df = pd.DataFrame(data, columns=['Model', 'RMSE'])

plt.plot(xgb_univariate_actual, label='Actual')
plt.plot(xgb_univariate_pred, label='XGB_uni Predicted')
plt.plot(xgb_multi_pred, label='XGB_multi Predicted')
plt.plot(rf_pred,label="RF Predicted")
plt.legend()
plt.show()

with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.precision', 4):
    print(df)