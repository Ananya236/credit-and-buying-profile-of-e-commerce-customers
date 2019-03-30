import numpy as np
import pandas as pd
from tkinter import *
from tkinter import messagebox
import xlrd
from xlutils.copy import copy
import shop

r=Tk()
r.geometry('1000x600')
r.title('LOGIN PAGE')
e1=Entry(r)
e1.place(x=450,y=100)
Label(r,text='USERNAME').place(x=380,y=100)
e2=Entry(r,show='*')
e2.place(x=450,y=180)
Label(r,text='PASSWORD').place(x=380,y=180)
def login():
    m1=e1.get()
    m2=e2.get()
    dw = xlrd.open_workbook('cust_details.xls')
    ds=dw.sheet_by_index(0)
    dnr1=ds.nrows                                 # this block opens sheet and counts its rows and columns
    dnc1=ds.ncols
    for i in range(1,dnr1):
        a=ds.cell_value(i,1)
        b=ds.cell_value(i,2)
        if(a==m1 and b==m2):
            messagebox.showinfo('LOGIN SUCCESSFUL','WELCOME TO SHOPPING')
            shop.main(ds.cell_value(i,0))
            '''r1=Tk()
            r1.geometry('1000x600')
            r1.title('LOGIN SUCCESSFUL') 
            Label(r1,text='WELCOME TO FACEBOOK').place(x=450,y=100)'''
            break
        if(i==dnr1-1):
            messagebox.showinfo('ERROR','Username or Password incorrect')
b1=Button(r,text='LOGIN',command=login)
b1.place(x=480,y=230)

def create():
    n1=p1.get()
    n2=p2.get()
    n3=p3.get()
    n4=p4.get()
    n5=p5.get()
    wb = xlrd.open_workbook('cust_details.xls')
    s=wb.sheet_by_index(0)
    wx=copy(wb)
    wr=wx.get_sheet(0)
    p=s.nrows
    n=0
    for i in range(1,p):
        a=s.cell_value(i,4)
        if(a==n4):
            messagebox.showwarning('ERROR','Number already exists')
            r2.destroy()
            n=1
            break
    if(len(n4)==10):
        n=0
    else:
        messagebox.showwarning('ERROR','Enter a valid number')
        r2.destroy()
        n=1
    if(n==0):
        if(n1=="" or n2=="" or n3=="" or n4=="" or n5==""):
            messagebox.showwarning('SIGNUP UNSUCCESSFULL','All fields are mandatory')
            r2.destroy()
        else:
            if(p==1):
                u_id=1001
            else:
                u_id=s.cell_value(p-1,0)
                u_id+=1
            wr.write(p,0,u_id);wr.write(p,1,n1);wr.write(p,2,n2);wr.write(p,3,n3);wr.write(p,4,n4);wr.write(p,5,n5)
            messagebox.showinfo('SIGNUP SUCCESSFULL','Ho Ho Ho Ho')
        wx.save('cust_details.xls')

def signup():
    global r2,p1,p2,p3,p4,p5     
    r2=Tk()
    r2.geometry('1000x600')
    r2.title('SIGNUP PAGE')
    Label(r2,text='PLEASE FILL IN YOUR DETAILS').place(x=450,y=100)
    p1=Entry(r2)
    p1.place(x=450,y=150)
    Label(r2,text='USERNAME').place(x=350,y=150)
    p2=Entry(r2,show='*')
    p2.place(x=450,y=180)
    Label(r2,text='PASSWORD').place(x=350,y=180)
    p3=Entry(r2)
    p3.place(x=450,y=210)
    Label(r2,text='E-MAIL ID').place(x=350,y=210)
    p4=Entry(r2)
    p4.place(x=450,y=240)
    Label(r2,text='PHONE NUMBER').place(x=350,y=240)
    p5=Entry(r2)
    p5.place(x=450,y=270)
    Label(r2,text='ADDRESS').place(x=350,y=270)
    b1=Button(r2,text='CREATE ACCOUNT',command=create)
    b1.place(x=450,y=310)


Label(r,text='New User?').place(x=475,y=340)
b1=Button(r,text='SIGNUP',command=signup)
b1.place(x=480,y=370)
r.mainloop()

