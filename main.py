from tkinter import *
from tkinter.ttk import Style


n1=0;c=1;temp1= " ";m=0;m1=0;d=[]

root =Tk()
root.geometry('385x420')
root.resizable(0,0)
root.title("simple calculator")


k = Entry(root,width =50,borderwidth=5)
k.grid(row=1,column=0,columnspan=4,padx=10,pady=10)
k1 = Entry(root,width =50,borderwidth=5)
k1.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


def schar(b):
    global n1,d,temp1,m
    if b=="=":
        d.append(str(n1))
        k1.delete(0,END)
        b1= "".join(d) +b
        k1.insert(0,b1)
        if "**" in d:
            z= d.count("**")
            for _ in range(z):
                o = d.index("**")
                x=float(d[o-1])**float(d[o+1])
                d.pop(o-1)
                d.pop(o-1)
                d.pop(o-1)
                if o>len(d):
                    d.append(str(x))
                else:
                    d.insert(o-1,str(x))
        if  "/" in d:
            z= d.count("/")
            for _ in range(z):
                o = d.index("/")
                x=float(d[o-1])/float(d[o+1])
                d.pop(o-1)
                d.pop(o-1)
                d.pop(o-1)
                if o>len(d):
                    d.append(str(x))
                else:
                    d.insert(o-1,str(x))
        if  "*" in d:
            z= d.count("*")
            for _ in range(z):
                o = d.index("*")
                x=float(d[o-1])*float(d[o+1])
                d.pop(o-1)
                d.pop(o-1)
                d.pop(o-1)
                if o>len(d):
                    d.append(str(x))
                else:
                    d.insert(o-1,str(x))
        if  "+" in d:
            z= d.count("+")
            for _ in range(z):
                o = d.index("+")
                x=float(d[o-1])+float(d[o+1])
                d.pop(o-1)
                d.pop(o-1)
                d.pop(o-1)
                if o>len(d):
                    d.append(str(x))
                else:
                    d.insert(o-1,str(x))
        if  "-" in d:
            z= d.count("-")
            for _ in range(z):
                o = d.index("-")
                x=float(d[o-1])-float(d[o+1])
                d.pop(o-1)
                d.pop(o-1)
                d.pop(o-1)
                if o>len(d):
                    d.append(str(x))
                else:
                    d.insert(o-1,str(x))
        
        if k.get()=="0":
            d=[]
            n1=0
            k.delete(0,END)
            k.insert(0,0)
            k1.delete(0,END)
        elif len(d)==1:
            k.delete(0,END)
            k.insert(0,str(d[0]))
        else:
            k.delete(0,END)
            k.insert(0,0)


    elif (len(d)==0 and b=="-") and m==0:
        k.insert(0,"-")
        m=1

    elif len(d)>0 and((temp1 in ["+","-","*","/"])and b=="-" ) and m==0 :
            k.insert(0,"-")
            print(k.get())
            m=1

    else:
        k.delete(0,END)
        d.append(str(n1))
        d.append(b)
        k1.delete(0,END)
        k1.insert(0,"".join(d))
        m=0
    temp1=b


def button_click(a):
    global n1,c,m
    current=str(k.get())
    k.delete(0,END)
    k.insert(0,current+str(a))
    n1 =float(current+str(a))



def button_clicks(bbb):
    global n1,m
    current = str(k.get())
    k.delete(0, END)
    if current =="-" and bbb==".":
        k.insert(0,  current +"0" + str(bbb))
        n1 = float( current +"0" + str(bbb))
    elif bbb == "." and current.count(".") == 0:
        if len(current) == 0:
            k.insert(0, "0"+current + str(bbb))
            n1 = float("0"+current + str(bbb))
        else:
            k.insert(0, current + str(bbb))
            n1 = float(current + str(bbb))
    elif bbb == "." and current.count(".") == 0:
        k.insert(0, "0" + current + str(bbb))
        n1 = float("0" + current + str(bbb))
    else:
        k.insert(0, current)
        n1= float(current)
    m=1
def button_clear():
    global n1,d,m
    k.delete(0,END)
    k1.delete(0,END)
    n1= 0;d=[]
    m=0


def button_cleare():
    global n1,d,m
    if len(k.get())>2:
        n1 = k.get()[0:-2]
    elif len(k.get()) ==2:
        n1= k.get()[0]
    else:
        n1=""
        m=0
    k.delete(0,END)
    k.insert(0,str(n1))

button_1=Button(root,text="1", padx=40,pady=20,command=lambda: button_click(1))
button_2=Button(root,text="2", padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3", padx=40,pady=20,command=lambda: button_click(3))
button_4=Button(root,text="4", padx=40,pady=20,command=lambda: button_click(4))
button_5=Button(root,text="5", padx=40,pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6", padx=40,pady=20,command=lambda: button_click(6))
button_7=Button(root,text="7", padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(root,text="8", padx=40,pady=20,command=lambda: button_click(8))
button_9=Button(root,text="9", padx=40,pady=20,command=lambda: button_click(9))
button_0=Button(root,text="0", padx=40,pady=20,command=lambda: button_click(0))
button_DOT=Button(root,text=".", padx=41.2,pady=20,command=lambda: button_clicks("."))
button_add=Button(root,text="+", padx=38.48,pady=20,command=lambda: schar("+"))
button_sub=Button(root,text="-", padx=40,pady=20,command=lambda: schar("-"))
button_mul=Button(root,text="*", padx=40,pady=20,command=lambda: schar("*"))
button_div=Button(root,text="/", padx=40,pady=20,command=lambda: schar("/"))
button_pow=Button(root,text="pow", padx=31,pady=20,command=lambda: schar("**"))
button_equal=Button(root,text="=", padx=39,pady=20,command=lambda:schar("="))
button_clrae=Button(root,text="Clear", padx=77,pady=20,command=button_clear)
button_clraee=Button(root,text="<-", padx=36,pady=20,command=button_cleare)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_clraee.grid(row=2,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_add.grid(row=3,column=3)


button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_sub.grid(row=4,column=3)


button_0.grid(row=5,column=0)
button_DOT.grid(row=5,column=1)
button_equal.grid(row=5,column=2)
button_mul.grid(row=5,column=3)


button_clrae.grid(row=6,column=0,columnspan=2)
button_pow.grid(row=6,column=2)
button_div.grid(row=6,column=3)

root.mainloop()
