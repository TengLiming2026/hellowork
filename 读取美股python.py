import pandas_datareader.data as web
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline


tc="TSLA"
start = datetime.datetime(2023,1,1)
end   = datetime.datetime(2026,2,2)

data = web.DataReader(tc,'yahoo',start,end)

SP500 = web.DataReader("SPY",'yahoo',start,end).Close #收盘价

SP500_return = SP500.pct_change().dropna()   # 计算日收益率
#SP500_return1= (SP500['Close']/SP500['Close'].shift(1)) - 1

#SP500_return2= (SP500['Close'].pct_change().fillna(0) 
#SP500_return3= (SP500['Close'].pct_change().dropna()   # 计算日收益率





SP500_return.name = 'SP500_return'   
@TengLiming2026
Comment
