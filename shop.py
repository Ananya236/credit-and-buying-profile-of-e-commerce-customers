import xlrd
import xlwt
from xlutils.copy import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import ses

t=time.ctime()

'''def add(a,i):
    count[a]+=1
    print(count)

    print(i)
    Label(fr,text=str(count[a]),font=(40)).grid(row=i,column=3)
    #val.config(text=str(count))

def remove(a,i):
    count[a]-=1
    Label(fr,text=count[a],font=(40)).grid(row=i,column=3)
    #val.config(text=count)'''
def update(u_id):
    global indx
    wb_retail = xlrd.open_workbook('retail.xls')
    s1=wb_retail.sheet_by_index(0)
    wx_retail=copy(wb_retail)
    wr_retail=wx_retail.get_sheet(0)
    p=s1.nrows
    for i in range (len(e)):
        count.append(int(e[i].get()))
        if(count[i]!=0):
            wr_retail.write(p,0,u_id);wr_retail.write(p,1,ds.cell_value(i+1,0));wr_retail.write(p,2,count[i]);wr_retail.write(p,3,ds.cell_value(i+1,3));wr_retail.write(p,4,ds.cell_value(i+1,3)-ds.cell_value(i+1,2));wr_retail.write(p,5,t);
            wx_retail.save("retail.xls")
            purchase[indx]=str(ds.cell_value(i+1,0)+"  "+str(count[i])+"  "+str(ds.cell_value(i+1,3)))
            indx+=1
            #print(purchase)
            wr_shop.write(i+1,1,int(ds.cell_value(i+1,1))-count[i])
            wx_shop.save("shop.xls")

def buy(u_id):
    update(u_id)
    main(u_id)                                                                                        

def generate(u_id):
    #global purchase,index
    #index=0
    #purchase={}
    update(u_id)
    dw_new = xlrd.open_workbook('new1p.xls')
    ds_new=dw_new.sheet_by_index(0)
    wx_new=copy(dw_new)
    wr_new=wx_new.get_sheet(0)
    bill=Frame(root)
    bill.grid(row=0,column=0,sticky="news")
    bill.tkraise()
    Label(bill,text='Thank You!! for shopping with us',font=('Aerial 50 bold')).grid(row=0,column=1)
    Label(bill,text='Product  Qty  Price',font=('Chiller 30 bold')).grid(row=1,column=1)
    n=0
    total=0
    pur=[]
    for i in range(len(purchase)):
        Label(bill,text = purchase[i],font=('Aerial 25')).grid(row=i+2,column=1)
        pur=purchase[i].split('  ')
        total+=int(pur[1])*float(pur[2])
        n=i+2
    Label(bill,text='',font=('Aerial 25')).grid(row=n+1,column=1)
    Label(bill,text='total      '+str(total),font=('Aerial 25')).grid(row=n+2,column=1)
    temp=0
    for i in range(ds_new.nrows):
        if(ds_new.cell_value(i,0)==str(int(u_id))):
            wr_new.write(i,6,ds_new.cell_value(i,6)+total)
            wr_new.write(i,7,ds_new.cell_value(i,7)+total)
            wr_new.write(i,8,ds_new.cell_value(i,8)+total)
            temp=1
            break
    if(temp==0):
        wr_new.write(ds_new.nrows,0,str(int(u_id)))
        wr_new.write(ds_new.nrows,1,0)
        wr_new.write(ds_new.nrows,2,0)
        wr_new.write(ds_new.nrows,3,0)
        wr_new.write(ds_new.nrows,4,0)
        wr_new.write(ds_new.nrows,5,0)
        wr_new.write(ds_new.nrows,6,total)
        wr_new.write(ds_new.nrows,7,total*1.2)
        wr_new.write(ds_new.nrows,8,total)
        wr_new.write(ds_new.nrows,9,0)
    wx_new.save("new1p.xls")
    ses.main()
    #Radiobutton(bill,text='COD',command=payment).grid(row=1,column=1)
       
def items(index,u_id):
    global count,ds,dw,wr_shop,wx_shop,e
    global purchase,indx
    indx=0
    purchase={}
    count=[]
    e=[]
    #b1=[]
    #b2=[]
    dw = xlrd.open_workbook('shop.xls')
    ds=dw.sheet_by_index(index)
    wx_shop=copy(dw)
    wr_shop=wx_shop.get_sheet(index)
    dr=ds.nrows
    fr.tkraise()
    Label(fr,text=ds.name,font=('Aerial 50 bold')).grid(row=0,column=1)
    for i in range(1,dr):
        Label(fr,text=str(ds.cell_value(i,0)),font=('Chiller',40)).grid(row=i,column=1)
        e.append(Entry(fr))
        e[i-1].insert(0,'0')
        e[i-1].grid(row=i,column=2)
        '''b1.append(Button(fr,text='+',command=lambda: add(str(ds.cell_value(i,0)),i)).grid(row=i,column=2))
        #Label(fr,text=str(count[str(ds.cell_value(i,0))]),font=(40)).grid(row=i,column=3)
        b2.append(Button(fr,text='-',command=lambda: remove(str(ds.cell_value(b2,0)),i)).grid(row=i,column=4))'''
    Button(fr,text='Buy More',command=lambda: buy(u_id)).grid(row=dr,column=1)
    Button(fr,text='Generate Bill',command=lambda: generate(u_id)).grid(row=dr,column=2)
    
def main(u_id):
    global fr,root
    root=Tk()
    root.geometry('1200x800')
    root.title('SHOPPING')
    r=Frame(root)
    r.grid(row=0,column=0,sticky='news')
    fr=Frame(root)
    fr.grid(row=0,column=0,sticky='news')
    Label(r,text='Welcome to our shopping site',font=('Aerial 50 bold')).grid(row=0,column=1)
    img1=PhotoImage(master=r,file='cloth.png')#.resize((100,100),Image.ANTIALIAS))
    Label(r,image=img1).grid(row=1,column=1)
    '''cv=Canvas()
    cv.grid(row=1,column=1)
    cv.create_image(20,20,image=img1)'''
    b1=Button(r,text='CLOTHES',command=lambda: items(0,u_id))
    b1.grid(row=1,column=2)
    img2=PhotoImage(master=r,file="electronics.png")
    Label(r,image=img2).grid(row=2,column=1)
    b1=Button(r,text='ELECTRONICS',command=lambda: items(1,u_id))
    b1.grid(row=2,column=2)
    img3=PhotoImage(master=r,file="stationery.png")
    Label(r,image=img3).grid(row=3,column=1)
    b1=Button(r,text='STATIONARY',command=lambda: items(2,u_id))
    b1.grid(row=3,column=2)
    r.tkraise()
    r.mainloop()

#main()
