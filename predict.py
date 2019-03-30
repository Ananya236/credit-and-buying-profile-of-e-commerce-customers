import numpy as np
import pandas as pd
from tkinter import *
from tkinter import messagebox
import xlrd
from xlutils.copy import copy
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt

dfs = pd.read_excel("new.xls", sheet_name='Sheet1')
train=dfs.iloc[:]
test=dfs.iloc[:]
y_hat_avg = test.copy()
fit2 = SimpleExpSmoothing(np.asarray(train['month_1'])).fit(smoothing_level=0.6,optimized=False)
y_hat_avg['SES'] = fit2.forecast(len(test))
plt.figure(figsize=(16,8))
plt.plot(train['month_1'], label='Train')
plt.plot(test['month_1'], label='Test')
plt.plot(y_hat_avg['SES'], label='SES')
plt.legend(loc='best')
plt.show()
