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

def main():
    warnings.filterwarnings("ignore")
    dataset = pd.read_excel('new1p.xls')
    train = dataset.iloc[:,1:6]
    test = dataset.iloc[:,6]

    print(type(train))
    #print('test')
    #print(test.head())

    #test = pd.DataFrame(test)
    #test.columns = ['month_6']

    wb=xlrd.open_workbook('new1p.xls')
    ws=wb.sheet_by_index(0)
    wx=copy(wb)
    wr=wx.get_sheet(0)

    print('Prediction for month 6 as per SIMPLE EXPONENTIAL SMOOTHING ALGORITHM\n')
    acc=0
    for i in range(ws.nrows-1):
        dff1=dataset["month_1"][i]-dataset["month_2"][i]
        dff2=dataset["month_2"][i]-dataset["month_3"][i]
        dff3=dataset["month_3"][i]-dataset["month_4"][i]
        dff4=dataset["month_4"][i]-dataset["month_5"][i]

        a=0.1          # where 'a' is smoothing factor
        dff_avg = int(a*dff4 + a*(1-a)*dff3 + a*((1-a)**2)*dff2 + a*((1-a)**3)*dff1)
        pred_month_6 = dff_avg+dataset["month_5"][i]
        print(pred_month_6)
        wr.write(i+1,22,int(pred_month_6))
        acc = acc + (abs(dataset["month_6"][i]-pred_month_6)/(dataset["month_6"][i]))*100

    print('Accuracy of prediction--\n')
    acc = acc/117
    print(acc)

    c=0
    for i in range(ws.nrows-1):
        dff1=dataset["month_1"][i]-dataset["month_2"][i]
        dff2=dataset["month_2"][i]-dataset["month_3"][i]
        dff3=dataset["month_3"][i]-dataset["month_4"][i]
        dff4=dataset["month_4"][i]-dataset["month_5"][i]
        dff5=dataset["month_5"][i]-dataset["month_6"][i]

        a=0.1          # where 'a' is smoothing factor
        dff_avg = int(a*dff5 + a*(1-a)*dff4 + a*((1-a)**2)*dff3 + a*((1-a)**3)*dff2 + a*((1-a)**4)*dff1)
        pred_month_7 = dff_avg+dataset["month_6"][i] 
        pred_cancel_7 = round(int(dataset["cancel"][i])/6)
        if(pred_cancel_7!=0):
            ratio = int(pred_month_7)/((pred_cancel_7)*100)
        else:
            ratio = 15
        if(ratio>15):
            wr.write(i+1,13,'P')
        else:
            wr.write(i+1,13,'N')
        wr.write(i+1,10,int(pred_month_7))
        wr.write(i+1,11,int(pred_cancel_7))
        wr.write(i+1,12,ratio)
        

    wx.save('new1p.xls')


    #wx.save(r'C:\Users\ANKIT\Downloads\C++\C++\file\text3.xls')

    y_hat_avg = test.copy()
    print('*******\n')
    fit2 = SimpleExpSmoothing(np.asarray(train['month_1'])).fit(smoothing_level=0.6,optimized=False)
    y_hat_avg['SES'] = fit2.forecast(len(test))
    plt.figure(figsize=(16,8))
    #plt.plot(train['month_1'], label='month_1')
    #plt.plot(train['month_2'], label='month_2')
    #plt.plot(train['month_3'], label='month_3')
    #plt.plot(train['month_4'], label='month_4')
    #plt.plot(train['month_5'], label='month_5')
    plt.plot(dataset['month_6'], label='month_6')
    plt.plot(dataset['pred_month_6'], label='pred_month_6')
    #plt.plot(dataset['pred_month_7'], label='pred_month_7')
    #print('&*&%*&%*%\n\n')
    #print(test.columns)
    #plt.plot(test, label='month_6')
    #plt.plot(y_hat_avg['SES'], label='SES')
    plt.legend(loc='best')
    plt.show()
