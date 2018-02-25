import sqlite3
from tkinter import *
import random
import time
import datetime
import numbers
from tkinter import messagebox
connection = sqlite3.connect('Bills.db')
cursor = connection.cursor()
root = Tk()

root.title("Cafe Billing System")

Tops = Frame(root, width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)
Bottoms = Frame(root, width=1350, height=50, bd=8, relief="raise")
Bottoms.pack(side=BOTTOM)

f1 = Frame(root, width=1400, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f1a = Frame(f1, width=1200, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=1200, height=320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=600, height=450, bd=8, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=600, height=430, bd=8, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=8, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=8, relief="raise")
f2ab.pack(side=LEFT)

f2 = Frame(root, width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

lblInfo = Label(Tops, font=('arial', 20, 'bold'), fg="brown",text="CAFE NAS", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblcopyright = Label(Bottoms, font=('arial', 10, 'italic'),fg="brown", text="Created by Anand,Neeraj and Shashank", bd=0, anchor='w')
lblcopyright.grid(row=0, column=0)
#==============================Variables=====================
PaymentRef=StringVar()
vegBurgers=StringVar()
chickenBurgers=StringVar()
vegSandwich=StringVar()
nvegSandwich=StringVar()
frenchFries=StringVar()
softDrinks=StringVar()
vPizza=StringVar()
nPizza=StringVar()
costvegBurgers=StringVar()
costchickenBurgers=StringVar()
costvegSandwich=StringVar()
costnvegSandwich=StringVar()
costfrenchFries=StringVar()
costsoftDrinks=StringVar()
costvPizza=StringVar()
costnPizza=StringVar()
dateRef=StringVar()
subTotal=StringVar()
vat=StringVar()
totalPrice=StringVar()
text_Input = StringVar()
dateRef.set(time.strftime("%d/%m/%y %H:%M:%S"))
operator = ""
vat.set(0)
PaymentRef.set(0)
vegBurgers.set(0)
chickenBurgers.set(0)
vegSandwich.set(0)
nvegSandwich.set(0)
frenchFries.set(0)
softDrinks.set(0)
vPizza.set(0)
nPizza.set(0)
subTotal.set(0)
totalPrice.set(0)
costvegBurgers.set(140)
costchickenBurgers.set(160)
costvegSandwich.set(100)
costnvegSandwich.set(120)
costsoftDrinks.set(20)
costfrenchFries.set(80)
costnPizza.set(200)
costvPizza.set(180)

#=============================Functions==================
def tPrice():
    vBprice=int(costvegBurgers.get())
    cBprice=int(costchickenBurgers.get())
    vSprice=int(costvegSandwich.get())
    nSprice=int(costnvegSandwich.get())
    fFprice=int(costfrenchFries.get())
    sDprice=int(costsoftDrinks.get())
    vPprice=int(costvPizza.get())
    nPprice=int(costnPizza.get())

    vBno=int(vegBurgers.get())
    cBno=int(chickenBurgers.get())
    vSno=int(vegSandwich.get())
    nSno=int(nvegSandwich.get())
    fFno=int(frenchFries.get())
    sDno=int(softDrinks.get())
    vPno=int(vPizza.get())
    nPno=int(nPizza.get())
    tempVat=int(vat.get())
    subPrice=(vBprice*vBno+cBprice*cBno+vSprice*vSno+nSprice*nSno+vPprice*vPno+nPprice*nPno+fFprice*fFno+sDprice*sDno)
    totalCost=str('%d'%subPrice),"Rs"
    totalCostwithVat=str('%d'%(subPrice +(subPrice*tempVat)/100)),"Rs"
    subTotal.set(totalCost)
    totalPrice.set(totalCostwithVat)
    
    


def iExit():
    qexit= messagebox.askyesno("Billing System", "Do you want to exit?")
    if qexit>0:
        root.destroy()
        return

def reset():
    PaymentRef.set(0)
    vegBurgers.set(0)
    chickenBurgers.set(0)
    vegSandwich.set(0)
    nvegSandwich.set(0)
    vPizza.set(0)
    nPizza.set(0)
    frenchFries.set(0)
    softDrinks.set(0)
    subTotal.set(0)
    totalPrice.set(0)

def refNo():
   refno=int(PaymentRef.get())

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

    
    


# ==============Calculator=============================
txtDisplay = Entry(f2, font=('arial', 10, 'bold'), textvariable=text_Input, bd=40, insertwidth=6, justify='right')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="7",
              command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="8",
              command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="9",
              command=lambda: btnClick(9)).grid(row=1, column=2)
btnPlus = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="+",
                 command=lambda: btnClick("+")).grid(row=1, column=3)
# ---------------
btn4 = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="4",
              command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8,fg="brown", font=('arial', 10, 'bold'), text="5",
              command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="6",
              command=lambda: btnClick(6)).grid(row=2, column=2)
btnSub = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="-",
                command=lambda: btnClick("-")).grid(row=2, column=3)
# --------------
btn1 = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="1",
              command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="2",
              command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="3",
              command=lambda: btnClick(3)).grid(row=3, column=2)
btnMult = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="*",
                 command=lambda: btnClick("*")).grid(row=3, column=3)
# --------------
btn0 = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="0",
              command=lambda: btnClick(0)).grid(row=4, column=0)
btnClear = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="C",
                  command=btnClearDisplay).grid(row=4, column=1)
btnEquals = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="=",
                   command=btnEqualsInput).grid(row=4, column=2)
btnDiv = Button(f2, padx=16, pady=16, bd=8, fg="brown", font=('arial', 10, 'bold'), text="/",
                command=lambda: btnClick("/")).grid(row=4, column=3)
#==================================Order Info===========================
lblRef=Label(f1aa,font=('arial',12,'bold'),fg="blue",text="Reference No", bd=16, justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1aa,font=('arial',12,'bold'),textvariable=PaymentRef, bd=10,insertwidth=2, justify='left')
txtRef.grid(row=0,column=1)

ref_no=txtRef.get();
# --------------
lblVb=Label(f1aa,font=('arial',12,'bold'),fg="green",text="Veg Burger", bd=16, justify='left')
lblVb.grid(row=1,column=0)
txtVb=Entry(f1aa,font=('arial',12,'bold'),textvariable=vegBurgers, bd=10,insertwidth=2, justify='left')
txtVb.grid(row=1,column=1)
# --------------
lblCb=Label(f1aa,font=('arial',12,'bold'),fg="red",text="Chicken Burger", bd=16, justify='left')
lblCb.grid(row=2,column=0)
txtCb=Entry(f1aa,font=('arial',12,'bold'),textvariable=chickenBurgers, bd=10,insertwidth=2, justify='left')
txtCb.grid(row=2,column=1)
# --------------
lblVs=Label(f1aa,font=('arial',12,'bold'),fg="green",text="Veg Sandwich", bd=16, justify='left')
lblVs.grid(row=3,column=0)
txtVs=Entry(f1aa,font=('arial',12,'bold'),textvariable=vegSandwich, bd=10,insertwidth=2, justify='left')
txtVs.grid(row=3,column=1)
# --------------
lblCs=Label(f1aa,font=('arial',12,'bold'),fg="red",text="Chicken Sandwich", bd=16, justify='left')
lblCs.grid(row=4,column=0)
txtCs=Entry(f1aa,font=('arial',12,'bold'),textvariable=nvegSandwich, bd=10,insertwidth=2, justify='left')
txtCs.grid(row=4,column=1)
# --------------
lblVp=Label(f1aa,font=('arial',12,'bold'),fg="green",text="Veg Pizza", bd=16, justify='left')
lblVp.grid(row=5,column=0)
txtVp=Entry(f1aa,font=('arial',12,'bold'),textvariable=vPizza, bd=10,insertwidth=2, justify='left')
txtVp.grid(row=5,column=1)
# --------------
lblCp=Label(f1aa,font=('arial',12,'bold'),fg="red",text="Chicken Pizza", bd=16, justify='left')
lblCp.grid(row=6,column=0)
txtCp=Entry(f1aa,font=('arial',12,'bold'),textvariable=nPizza, bd=10,insertwidth=2, justify='left')
txtCp.grid(row=6,column=1)
# --------------
lblFf=Label(f1aa,font=('arial',12,'bold'),fg="green",text="French Fries", bd=16, justify='left')
lblFf.grid(row=7,column=0)
txtFf=Entry(f1aa,font=('arial',12,'bold'),textvariable=frenchFries, bd=10,insertwidth=2, justify='left')
txtFf.grid(row=7,column=1)
# --------------
lblSd=Label(f1aa,font=('arial',12,'bold'),fg="green",text="Soft Drinks/Beverages", bd=16, justify='left')
lblSd.grid(row=8,column=0)
txtSd=Entry(f1aa,font=('arial',12,'bold'),textvariable=softDrinks, bd=10,insertwidth=2, justify='left')
txtSd.grid(row=8,column=1)

#===================================Payment Info==========================
lbldate=Label(f1ab,font=('arial',12,'bold'),fg="blue",text="Date", bd=16, justify='left')
lbldate.grid(row=0,column=0)
txtdate=Entry(f1ab,font=('arial',12,'bold'),textvariable=dateRef, bd=10,insertwidth=2, justify='left')
txtdate.grid(row=0,column=1)

date=txtdate.get();
# --------------
lblCvb=Label(f1ab,font=('arial',12,'bold'),fg="green",text="Price of Veg Burger", bd=16, justify='left')
lblCvb.grid(row=1,column=0)
txtCvb=Entry(f1ab,font=('arial',12,'bold'),textvariable=costvegBurgers, bd=10,insertwidth=2, justify='left')
txtCvb.grid(row=1,column=1)
# --------------
lblCsd=Label(f1ab,font=('arial',12,'bold'),fg="green",text="Price of Soft Drinks/Beverages", bd=16, justify='left')
lblCsd.grid(row=8,column=0)
txtCsd=Entry(f1ab,font=('arial',12,'bold'),textvariable=costsoftDrinks, bd=10,insertwidth=2, justify='left')
txtCsd.grid(row=8,column=1)
# --------------
lblCvs=Label(f1ab,font=('arial',12,'bold'),fg="green",text="Price of Veg Sandwich", bd=16, justify='left')
lblCvs.grid(row=3,column=0)
txtCvs=Entry(f1ab,font=('arial',12,'bold'),textvariable=costvegSandwich, bd=10,insertwidth=2, justify='left')
txtCvs.grid(row=3,column=1)
# --------------
lblCcs=Label(f1ab,font=('arial',12,'bold'),fg="red",text="Price of Chicken Sandwich", bd=16, justify='left')
lblCcs.grid(row=4,column=0)
txtCcs=Entry(f1ab,font=('arial',12,'bold'),textvariable=costnvegSandwich, bd=10,insertwidth=2, justify='left')
txtCcs.grid(row=4,column=1)
# --------------
lblCvp=Label(f1ab,font=('arial',12,'bold'),fg="green",text="Price of Veg Pizza", bd=16, justify='left')
lblCvp.grid(row=5,column=0)
txtCvp=Entry(f1ab,font=('arial',12,'bold'),textvariable=costvPizza, bd=10,insertwidth=2, justify='left')
txtCvp.grid(row=5,column=1)
# --------------
lblCcp=Label(f1ab,font=('arial',12,'bold'),fg="red",text="Price of Chicken Pizza", bd=16, justify='left')
lblCcp.grid(row=6,column=0)
txtCcp=Entry(f1ab,font=('arial',12,'bold'),textvariable=costnPizza, bd=10,insertwidth=2, justify='left')
txtCcp.grid(row=6,column=1)
# --------------
lblCcb=Label(f1ab,font=('arial',12,'bold'),fg="red",text="Price of Chicken Burger", bd=16, justify='left')
lblCcb.grid(row=2,column=0)
txtCcb=Entry(f1ab,font=('arial',12,'bold'),textvariable=costchickenBurgers, bd=10,insertwidth=2, justify='left')
txtCcb.grid(row=2,column=1)
# --------------
lblCff=Label(f1ab,font=('arial',12,'bold'),fg="green",text="Price of French Fries", bd=16, justify='left')
lblCff.grid(row=7,column=0)
txtCff=Entry(f1ab,font=('arial',12,'bold'),textvariable=costfrenchFries, bd=10,insertwidth=2, justify='left')
txtCff.grid(row=7,column=1)
#==========================Total Payment Info======
lblPrice=Label(f2aa,font=('arial',8,'bold'),fg="blue",text="Price", bd=16, justify='left')
lblPrice.grid(row=0,column=0)
txtPrice=Entry(f2aa,font=('arial',8,'bold'),textvariable=subTotal, bd=10,insertwidth=2, justify='left')
txtPrice.grid(row=0,column=1)
# --------------
lblVat=Label(f2aa,font=('arial',8,'bold'),fg="blue",text="TAX", bd=16, justify='left')
lblVat.grid(row=1,column=0)
txtVat=Entry(f2aa,font=('arial',8,'bold'),textvariable=vat, bd=10,insertwidth=2, justify='left')
txtVat.grid(row=1,column=1)
# --------------
lblTp=Label(f2aa,font=('arial',8,'bold'),fg="blue",text="Total Price", bd=16, justify='left')
lblTp.grid(row=2,column=0)
txtTp=Entry(f2aa,font=('arial',8,'bold'),textvariable=totalPrice, bd=10,insertwidth=2, justify='left')
txtTp.grid(row=2,column=1)
total_price=txtTp.get()
#==============Buttons==========

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS Bills(Ref No INTEGER,Date TEXT,Total Price INTEGER)')
    connection.commit()
create_table();


def entries():
    cursor.execute("INSERT INTO Bills VALUES(?,?,?)",(txtRef.get(),txtdate.get(),txtTp.get()))
    connection.commit()



btnTotal=Button(f2ab,padx=16,pady=16,bd=8, fg="brown",font=('arial',8,'bold'),width=15,
                text="Total Price",command=tPrice).grid(row=0,column=0)
btnBill=Button(f2ab,padx=16,pady=16,bd=8, fg="brown",font=('arial',8,'bold'),width=15,
                text="Create Bill",command=entries).grid(row=0,column=1)
btnReset=Button(f2ab,padx=16,pady=16,bd=8, fg="brown",font=('arial',8,'bold'),width=15,
                text="Reset",command=reset).grid(row=1,column=0)
btnExit=Button(f2ab,padx=16,pady=16,bd=8, fg="brown",font=('arial',8,'bold'),width=15,
                text="Exit",command=iExit).grid(row=1,column=1)

img2=PhotoImage(file="cafe1.png")
label2=Label(root,image=img2)
label2.pack()

img1=PhotoImage(file="sandwich.png")
label1=Label(root,image=img1)
label1.pack()
img3=PhotoImage(file="pizza.png")
label3=Label(root,image=img3)
label3.pack()
img4=PhotoImage(file="burger.png")
label4=Label(root,image=img4)
label4.pack()
img5=PhotoImage(file="fries.png")
label5=Label(root,image=img5)
label5.pack()


root.mainloop()
