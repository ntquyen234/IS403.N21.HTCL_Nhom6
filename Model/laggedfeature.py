import numpy as np
import pandas as pd 

def set(n_lag, y):
    lagged_feature = np.array(0)
    n = len(y) - n_lag

    for i in range(0, n_lag-1):
        lagged_feature = np.append(lagged_feature, 0)

    for i in range(0, n):
        sum = 0
        for j in range(i+n_lag-1, i - 1, -1):
            sum = sum + y.iloc[j]
        mean = sum / n_lag
        # if mean < y.iloc[n_lag-1]:
        #     mean = y.iloc[n_lag-1]
        lagged_feature = np.append(lagged_feature, mean)

    return lagged_feature

def set_30(n_lag, y):
    lagged_feature = np.array(np.sum(y[:-1].tail(n_lag))/n_lag)
    last_lagged_prices = np.array(y.tail(n_lag))
    n = len(y) - n_lag        

    for i in range(1, 30):
        sum = np.sum(last_lagged_prices)
        mean = sum / n_lag
        
        lagged_feature = np.append(lagged_feature, mean)
        last_lagged_prices = np.append(last_lagged_prices, mean)
        last_lagged_prices = last_lagged_prices[-n_lag:]

    return pd.DataFrame(lagged_feature)