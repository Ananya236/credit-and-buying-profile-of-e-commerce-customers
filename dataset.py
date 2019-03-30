import pandas as pd
import numpy as np
import random
import string
import warnings
from pandas import ExcelWriter

warnings.filterwarnings("ignore")

data = pd.read_csv('flip.csv')
df = pd.DataFrame(data,columns=['retail_price','discounted_price'])
df1=df.iloc[0:50]
#df2=df1.groupby('uniq_id')['retail_price'].apply(list)
#for i in range(0,200):
#def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    #return ''.join(random.choice(chars) for _ in range(size))

def decomposition(i):
        num=i
        while i > 0:
            n = random.randint(1, int(num/5)+1)
            yield n
            i -= n

df1["discounted_price"].fillna(6, inplace = True)
df1["retail_price"].fillna(0, inplace = True)
#df1 = df1[df1.retail_price.notnull()]  #for removing NaN values
df1.insert(0, "user_id",'0')
df1.insert(1, "month_1",0)
df1.insert(2, "month_2",0)
df1.insert(3, "month_3",0)
df1.insert(4, "month_4",0)
df1.insert(5, "month_5",0)
df1.insert(6, "month_6",0)
print(df1)

c=0
for j in range(len(df1)):
    a=[]
    while(len(a)!=6):
        a=list(decomposition(df1["discounted_price"][j]))
    for i in range(0,6):
        if(i==0):
            df1["month_1"][c]=a[i]  
        if(i==1):
            df1["month_2"][c]=a[i]    
        if(i==2):
            df1["month_3"][c]=a[i]    
        if(i==3):
            df1["month_4"][c]=a[i]    
        if(i==4):
            df1["month_5"][c]=a[i]    
        if(i==5):
            df1["month_6"][c]=a[i]
    c=c+1
print("ho ho ho ho")
df1.insert(9, "cancel",0)
user_id = pd.Series([])
cancel = pd.Series([])
for k in range(len(df1)): 
    if df1["user_id"][k] == '0': 
        df1["user_id"][k]=(random.randrange(1, 150, 3))
        df1["cancel"][k]=(random.randrange(0, 3, 1))
        

df2=df1.groupby("user_id").sum()
print(df2)

writer=ExcelWriter('new.xls')
df2.to_excel(writer,'Sheet1')
writer.save()
