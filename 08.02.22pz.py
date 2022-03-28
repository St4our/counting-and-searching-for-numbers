from tkinter import *  
from tkinter import scrolledtext  
  
window = Tk()  
window.title("18-01-2022-Практическая работа")  
window.geometry('900x700')  

#_______раздел функций______
def kliner1():
    txt_pole.delete('1.0', END)

#1
def click1():  
    a=int(txt_a.get())
    #b=int(txt_b.get())
    i=0
    k=[]
    k_ch=[]
    k_nch=[]
    k_9=[]
    for i in range(a,b+1):
        k.append(i)
    for i in range (len(k)):
        if (k[i])%2!=0: #ищем нечетное число
            k_nch.append(i)
        else:
            k_ch.append(i)
    for i in range (len(k)):
        if k[i]%9!=1: #ищем число кратное 9
            k_9.append(i)
    s1=sum(k_nch)
    s2=sum(k_ch)
    s3=sum(k_9)
    txt_pole.insert("1.0",s2)
    txt_pole.insert("2.0","\n")      
    txt_pole.insert("3.0",s1)
    txt_pole.insert("4.0","\n")
    txt_pole.insert("5.0",s3)
    txt_pole.insert("6.0","\n")


    

#_______конец раздела функций____________
#1______
lbl_1=Label(window, text="Введите число", font=("Arial Bold", 15))  
lbl_1.grid(column=1, row=3)  

txt_a=Entry(window,width=40)  
txt_a.grid(column=1, row=4)

lbl_2=Label(window, text="Сумма: ", font=("Arial Bold", 15))  
lbl_2.grid(column=0, row=4)  

txt_pole =scrolledtext.ScrolledText(window, width=50,height=5)
txt_pole.grid(column=0, row=5)

lbl_3=Label(window, text="Количество цифр: ", font=("Arial Bold", 15))  
lbl_3.grid(column=0, row=2)  

txt_pole =scrolledtext.ScrolledText(window, width=50,height=5)
txt_pole.grid(column=0, row=3)

lbl_2=Label(window, text="Cреднее арифметическое: ", font=("Arial Bold", 15))  
lbl_2.grid(column=0, row=6)  

txt_pole =scrolledtext.ScrolledText(window, width=50,height=5)
txt_pole.grid(column=0, row=7)

lbl_2=Label(window, text="Kоличество нулей: ", font=("Arial Bold", 15))  
lbl_2.grid(column=0, row=8)  

txt_pole =scrolledtext.ScrolledText(window, width=50,height=5)
txt_pole.grid(column=0, row=9)



knopka=Button(window, text="Посчитать!", command=click1)  
knopka.grid(column=2, row=4) 




knopka1=Button(window, text="Очистить!", command=kliner1)  
knopka1.grid(column=3, row=4) 







window.mainloop()

