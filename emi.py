from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import pandas as pd
import numpy as np
import random
import string
import warnings
import xlwt
from xlutils.copy import *
from pandas import ExcelWriter
import matplotlib.pyplot as plt
from math import *
import xlrd

warnings.filterwarnings("ignore")
data = pd.read_excel('emi1p.xls')

wb=xlrd.open_workbook('emi1p.xls')
wx=copy(wb)
wr=wx.get_sheet(0)

avg_6=0
acc1=0
acc=0
for i in range(0,99):
    avg_6 = round((data['p_aug'][i]+data['p_july'][i]+data['p_june'][i]+data['p_may'][i]+data['p_april'][i])/6)
    wr.write(i+1,12,avg_6)
    if(data["p_sep"][i]==0):
        if(avg_6==0):
            acc=100
        elif(avg_6==1 or avg_6==-1):
            acc=50
        else:
            acc=25
    else:
        acc=(abs(data["p_sep"][i]-avg_6)/abs(data["p_sep"][i]))*100
    acc1 = acc1 + acc
    print(acc1)

print('Accuracy of prediction--\n')
acc1 = acc1/99
print(acc1)

avg=0
for i in range(0,99):
    avg = round((data['p_sep'][i]+data['p_aug'][i]+data['p_july'][i]+data['p_june'][i]+data['p_may'][i]+data['p_april'][i])/6)
    wr.write(i+1,10,avg)

for i in range(1,99):
    if(data['predicted'][i]<=0):
        wr.write(i+1,11,'YES')
    elif(0<data['predicted'][i]<2):
        wr.write(i+1,11,'MAYBE')
    else:
        wr.write(i+1,11,'NO')

wx.save('emi1p.xls')
plt.figure(figsize=(16,8))
plt.plot(data['p_sep'], label='p_sep')
plt.plot(data['pred_sep'], label='pred_sep')
plt.legend(loc='best')
plt.show()


