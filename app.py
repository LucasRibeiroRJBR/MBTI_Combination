from distutils.command.config import config
from tkinter import *
from tkinter import ttk
import db_mbti

def processar():
    a = db_mbti.MBTI('db/mbti.db').consultar(varYou,varTheir)
    print(a)
    #lb_spacer['text'] = f"From 1 to 5 -> {a[0][0]}\nLevel = {a[0][1]}"
    if a[0][0] == 1:
        lb_spacer['image'] = n1
    elif a[0][0] == 2:
        lb_spacer['image'] = n2
    elif a[0][0] == 3:
        lb_spacer['image'] = n3
    elif a[0][0] == 4:
        lb_spacer['image'] = n4
    elif a[0][0] == 5:
        lb_spacer['image'] = n5


font_1 = font=('Consolas 24 bold')
font_2 = font=('Consolas 14 bold')
font_3 = font=('Consolas 10 bold')

root = Tk()
root.geometry('344x400')
root.option_add("*TCombobox*Listbox*Font", font_3)

style = ttk.Style(root)
style.theme_use('vista')

n1 = PhotoImage(file='img/n1.png')
n2 = PhotoImage(file='img/n2.png')
n3 = PhotoImage(file='img/n3.png')
n4 = PhotoImage(file='img/n4.png')
n5 = PhotoImage(file='img/n5.png')

perfis = ('ENFJ','ENFP','ENTJ','ENTP','ESFJ','ESFP','ESTJ','ESTP','INFJ','INFP','INTJ','INTP','ISFJ','ISFP','ISTJ','ISTP')

lb = ttk.Label(root,text='Combinações MBTI',font=font_1)

lb_you = ttk.Label(root,text='YOU',font=font_2)
lb_their = ttk.Label(root,text='THEIR',font=font_2)

img_love = PhotoImage(file='img/love.png')
lb_love = ttk.Label(root,image=img_love)

varYou = StringVar()
cbx_you = ttk.Combobox(root,width=10,textvariable=varYou)
cbx_you['values'] = perfis

varTheir = StringVar()
cbx_their = ttk.Combobox(root,width=10,textvariable=varTheir)
cbx_their['values'] = perfis

bt_consultar = ttk.Button(root,command=processar)

lb_spacer = Label(root,text='')

lb.grid(row=0,columnspan=3,padx=25,pady=5)
lb_you.grid(row=1,column=0)
lb_their.grid(row=1,column=2)
lb_love.grid(row=1,rowspan=3,column=1)
cbx_you.grid(row=2,column=0)
cbx_their.grid(row=2,column=2)
bt_consultar.grid(row=4,column=1,pady=15)
lb_spacer.grid(row=5,columnspan=3)

root.mainloop()

