import pyupbit
import pandas as pd
import numpy as np

pd.set_option('display.float_format', lambda x: '%.2f' % x)
df = pyupbit.get_ohlcv("KRW-BTC")

df['vari'] = df['close'] - df['close'].shift(1)
df['inc_rate'] = np.where(df['vari']>=0, df['변화량'], 0)
df['dec_rate'] = np.where(df['vari'] <0, df['변화량'].abs(), 0)

# welles moving average
df['AU'] = df['상승폭'].ewm(alpha=1/14, min_periods=14).mean()
df['AD'] = df['하락폭'].ewm(alpha=1/14, min_periods=14).mean()
#df['RS'] = df['AU'] / df['AD']
#df['RSI'] = 100 - (100 / (1 + df['RS']))
df['RSI'] = df['AU'] / (df['AU'] + df['AD']) * 100
df[['RSI']].tail(n=10)

#RS input yet considered
