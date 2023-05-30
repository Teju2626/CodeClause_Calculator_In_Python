import sys
from tkinter import *

root=Tk()
root.title("calculator")
root.configure(bg="black")
root.geometry('350x400')
def clear():
    displaybox.delete(0,END)
def btnclick(num):
    current=displaybox.get()
    clear()
    firstnumber=current+num
    displaybox.insert(0,firstnumber)#starting index-0,insert-module

fi_num=0
math=''
def calc(mathtype):
    global fi_num,math
    math=mathtype
    fi_num=displaybox.get()
    clear()

def equal():
    global fi_num
    secondnum=displaybox.get()
    clear()
    if(math=='add'):
        result=int(fi_num)+int(secondnum)
    elif(math=='sub'):
        result=int(fi_num)-int(secondnum)
    elif(math=='mul'):
        result=int(fi_num)*int(secondnum)
    elif(math=='div'):
            
            
        result=int(fi_num)/int(secondnum)
    displaybox.insert(0,str(result))

        
        
        
displaybox=Entry(root,width=20,font=('arial',28),justify=RIGHT)
btn0=Button(root,text='0',padx=36,pady=11,font=('arial',18),command=lambda: btnclick('0'))
btn1=Button(root,text='1',padx=36,pady=11,font=('arial',18),command=lambda: btnclick('1'))
btn2=Button(root,text='2',padx=36,pady=11,font=('arial',18),command=lambda: btnclick('2'))
btn3=Button(root,text='3',padx=36,pady=11,font=('arial',18),command=lambda: btnclick('3'))
btn4=Button(root,text='4',padx=36,pady=11,font=('arial',18),command=lambda: btnclick('4'))
btn5=Button(root,text='5',padx=36,pady=11,font=('arial',18),command=lambda: btnclick('5'))
btn6=Button(root,text='6',padx=36,pady=11,font=('arial',18),command=lambda: btnclick('6'))

                                                                                    
btn7=Button(root,text='7',padx=36,pady=11,font=('arial',18),command=lambda: btnclick('7'))
btn8=Button(root,text='8',padx=36,pady=11,font=('arial',18),command=lambda: btnclick('8'))
btn9=Button(root,text='9',padx=36,pady=11,font=('arial',18),command=lambda: btnclick('9'))

btnclear=Button(root,text='clear',padx=80,pady=10,font=('arial',18),command=clear)
btndiv=Button(root,text='/',padx=39,pady=11,font=('arial',18),command=lambda:calc('div'))
btnmul=Button(root,text='*',padx=38,pady=11,font=('arial',18),command=lambda:calc('mul'))
btnsub=Button(root,text='-',padx=38,pady=11,font=('arial',18),command=lambda:calc('sub'))
btnadd=Button(root,text='+',padx=37,pady=11,font=('arial',18),command=lambda:calc('add'))
btnequal=Button(root,text='=',padx=37,pady=39,font=('arial',18),command=equal)

displaybox.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

btnclear.grid(row=4,column=1,columnspan=2,padx=2,pady=2)


btndiv.grid(row=5,column=0,padx=2,pady=2)
btnmul.grid(row=5,column=1,padx=2,pady=2)
btnsub.grid(row=6,column=0,padx=2,pady=2)
btnadd.grid(row=6,column=1,padx=2,pady=2)
btnequal.grid(row=5,column=2,rowspan=2,padx=2,pady=2)


btn0.grid(row=4,column=0,padx=2,pady=2)

btn1.grid(row=3,column=0,padx=2,pady=2)
btn2.grid(row=3,column=1,padx=2,pady=2)
btn3.grid(row=3,column=2,padx=2,pady=2)

btn4.grid(row=2,column=0,padx=2,pady=2)
btn5.grid(row=2,column=1,padx=2,pady=2)
btn6.grid(row=2,column=2,padx=2,pady=2)

btn7.grid(row=1,column=0,padx=2,pady=2)
btn8.grid(row=1,column=1,padx=2,pady=2)
btn9.grid(row=1,column=2,padx=2,pady=2)
root.mainloop()

