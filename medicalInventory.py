from Tkinter import *
import webbrowser 
import sqlite3
from tkMessageBox import *
    
con=sqlite3.Connection('myinventory')
cur=con.cursor()
cur.execute('create table if not exists inventory_db(med_name varchar(20),med_price number(5,2),med_qty number)')
root=Tk()
def insert():
    if a.get()!='' and b.get()!='' and c.get()!='':
        if a.get().isdigit() or b.get().isalpha() or c.get().isalpha():
            showerror('Error',"Invalid Information!!")
        else:
            cur.execute("insert into inventory_db values(?,?,?)",(a.get(),b.get(),c.get()))
            showinfo('Success','Insertion Successful!')
            con.commit()
    else:
        showerror('Error','Please Enter some detail to save record.')

def update():
    temp=str()
    if a.get()!='' and b.get()!='' and c.get()!='':
        '''if a.get().isdigit() or b.get().isaplha() or c.get().isaplha():
            showerror('Error',"Invalid Information!!"
        else:'''
        cur.execute("update inventory_db set med_price='"+b.get()+"'where med_name='"+a.get()+"'")
        cur.execute("update inventory_db set med_qty='"+c.get()+"'where med_name='"+a.get()+"'")
        con.commit()
        showinfo('Success','Record successfully updated!')

def delete():
    if a.get()!='':
        cur.execute("delete from inventory_db where med_name='"+a.get()+"'")
        showinfo('Success','Record successfully deleted!')
    else:
        showerror('Error','Please Enter detail to delete record!')
        con.commit()

def load():
    if a.get()!='':
        cur.execute("select * from inventory_db where med_name='"+a.get()+"'")
        z=cur.fetchone()
        showinfo('Result',z)
        
    else:
        showerror('Error','Please Enter detail to make Search!')

def display():
    disp=Tk()
    Label(disp,text="Medcname Price Quantity").grid(row=0)
    cur.execute("select * from inventory_db")
    z=1;
    for x in cur.fetchall():
        Label(disp,text=x).grid(row=z,columnspan=12)
        z=z+1
    #disp.geometry("500x500")
    disp.mainloop()
    
        
    
b1=PhotoImage(file="backgroundddd.gif")
bl1=Label(root,image=b1)
bl1.grid(rowspan=200,columnspan=12)

root.title('Medicine inventory')
root.geometry("400x400")
Label(root,text='Enter Medicine Name',bg='powder blue',font='Arial',fg="white",bd=2).grid(row=72,column=3,sticky=W)
a=Entry()
a.grid(row=72,column=4,sticky=E+W)
Label(root,text='Enter Medicine Price',bg='powder blue',font='Arial',fg="white",bd=2).grid(row=74,column=3,sticky=W)
b=Entry()
b.grid(row=74,column=4,sticky=E+W)
Label(root,text='Medicine Quantity',bg='powder blue',font='Arial',fg="white",bd=2).grid(row=76,column=3,sticky=W)
c=Entry()
c.grid(row=76,column=4,sticky=E+W)

Button(root,text=" Insert  ",bg="#e84c3d",fg="white",command=insert).grid(row=80,column=2)
Button(root,text="Update",bg="#e84c3d",fg="white",command=update).grid(row=84,column=2)
Button(root,text=" Delete ",bg="#e84c3d",fg="white",command=delete).grid(row=92,column=2)
Button(root,text="  Load  ",bg="#e84c3d",fg="white",command=load).grid(row=88,column=2)

def onclick1(x):
    a.insert(25,x)

def keybrd():
    kb=Tk()
    
    Button(kb,text="q",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('q')).grid(row=12,column=7,sticky=N+W+S+E)
    Button(kb,text="w",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('w')).grid(row=12,column=8,sticky=N+W+S+E)
    Button(kb,text="e",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('e')).grid(row=12,column=9,sticky=N+W+S+E)
    Button(kb,text="r",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('r')).grid(row=12,column=10,sticky=N+W+S+E)
    Button(kb,text="t",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('t')).grid(row=12,column=11,sticky=N+W+S+E)
    Button(kb,text="y",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('y')).grid(row=12,column=12,sticky=N+W+S+E)
    Button(kb,text="u",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('u')).grid(row=12,column=13,sticky=N+W+S+E)
    Button(kb,text="i",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('i')).grid(row=12,column=14,sticky=N+W+S+E)
    Button(kb,text="o",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('o')).grid(row=12,column=15,sticky=N+W+S+E)
    Button(kb,text="p",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('p')).grid(row=12,column=16,sticky=N+W+S+E)
    Button(kb,text="7",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('7')).grid(row=12,column=17,sticky=N+W+S+E)
    Button(kb,text="8",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('8')).grid(row=12,column=18,sticky=N+W+S+E)
    Button(kb,text="9",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('9')).grid(row=12,column=19,sticky=N+W+S+E)

    Button(kb,text="a",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('a')).grid(row=13,column=7,sticky=N+W+S+E)
    Button(kb,text="s",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('s')).grid(row=13,column=8,sticky=N+W+S+E)
    Button(kb,text="d",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('d')).grid(row=13,column=9,sticky=N+W+S+E)
    Button(kb,text="f",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('f')).grid(row=13,column=10,sticky=N+W+S+E)
    Button(kb,text="g",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('g')).grid(row=13,column=11,sticky=N+W+S+E)
    Button(kb,text="h",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('h')).grid(row=13,column=12,sticky=N+W+S+E)
    Button(kb,text="j",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('j')).grid(row=13,column=13,sticky=N+W+S+E)
    Button(kb,text="k",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('k')).grid(row=13,column=14,sticky=N+W+S+E)
    Button(kb,text="l",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('l')).grid(row=13,column=15,sticky=N+W+S+E)
    Button(kb,text="-",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('-')).grid(row=13,column=16,sticky=N+W+S+E)
    Button(kb,text="4",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('4')).grid(row=13,column=17,sticky=N+W+S+E)
    Button(kb,text="5",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('5')).grid(row=13,column=18,sticky=N+W+S+E)
    Button(kb,text="6",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('6')).grid(row=13,column=19,sticky=N+W+S+E)


    Button(kb,text="z",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('z')).grid(row=14,column=7,sticky=N+W+S+E)
    Button(kb,text="x",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('x')).grid(row=14,column=8,sticky=N+W+S+E)
    Button(kb,text="c",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('c')).grid(row=14,column=9,sticky=N+W+S+E)
    Button(kb,text="v",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('v')).grid(row=14,column=10,sticky=N+W+S+E)
    Button(kb,text="b",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('b')).grid(row=14,column=11,sticky=N+W+S+E)
    Button(kb,text="n",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('n')).grid(row=14,column=12,sticky=N+W+S+E)
    Button(kb,text="m",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('m')).grid(row=14,column=13,sticky=N+W+S+E)
    Button(kb,text=",",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1(',')).grid(row=14,column=14,sticky=N+W+S+E)
    Button(kb,text=".",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('.')).grid(row=14,column=15,sticky=N+W+S+E)
    Button(kb,text="/",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('/')).grid(row=14,column=16,sticky=N+W+S+E)
    Button(kb,text="1",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('1')).grid(row=14,column=17,sticky=N+W+S+E)
    Button(kb,text="2",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('2')).grid(row=14,column=18,sticky=N+W+S+E)
    Button(kb,text="3",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('3')).grid(row=14,column=19,sticky=N+W+S+E)

def contact():
    root.destroy()
    contactus()
def contactus():
    abhip=Tk()
    abhip.title('Contact Us')
    b3=PhotoImage(file="contact1.gif")
    bl3=Label(abhip,image=b3)
    bl3.grid(rowspan=200,columnspan=12)
    abhip.geometry("400x400")
    #def start():
        #abhip.destroy()
        #abhimain()
    url1 = 'https://www.facebook.com/'
    url2 = 'https://www.linkedin.com/'
    url3 = 'https://twitter.com/'
    def OpenUrl(url):
        webbrowser.open_new(url)
    
    Button(text='/MedicalInventory.com',bg="#e84c3d",fg="white",command=lambda aurl=url1:OpenUrl(aurl)).grid(row=76,column=8)
    Button(text='@medicalinventory      ',bg="#e84c3d",fg="white",command=lambda aurl=url2:OpenUrl(aurl)).grid(row=116,column=8)
    Button(text='@MedInvertory              ',bg="#e84c3d",fg="white",command=lambda aurl=url3:OpenUrl(aurl)).grid(row=156,column=8)
    #Button(text='HOME',command=start,bg="#e84c3d",fg="white").grid(row=192,column=11)
    
    abhip.mainloop()
    
Button(root,text="Contact us",command=contact,bg="#e84c3d",fg="white").grid(row=92,column=11)

Button(root,text=" Display   ",bg="#e84c3d",fg="white",command=display).grid(row=80,column=11)
Button(root,text="Keyboard",bg="#e84c3d",fg="white",command=keybrd).grid(row=84,column=11)

def locate():
    root.destroy()
    locateus()
def locateus():
    abhiloc=Tk()
    abhiloc.title('Locate Us')
    b4=PhotoImage(file="lacateus.gif")
    bl4=Label(abhiloc,image=b4)
    bl4.grid(rowspan=200,columnspan=12)
    abhiloc.geometry("400x400")
    def start():
        abhiloc.destroy()
        abhimain()
    url = 'https://www.google.co.in/maps/dir/''/''/@18.4294718,76.5078071,12z/data=!3m1!4b1!4m8!4m7!1m0!1m5!1m1!1s0x3bcf84716e4cfd71:0x57fbdd49740647a7!2m2!1d76.5778476!2d18.4294846'
    def OpenUrl(url):
        webbrowser.open_new(url)
    
    Button(text='Locate Us',bg="#e84c3d",fg="white",font='Arial 12 bold',command=lambda aurl=url:OpenUrl(aurl)).grid(row=76,column=8)

    abhiloc.mainloop()

Button(root,text="Location ",bg="#e84c3d",fg="white",command=locate).grid(row=88,column=11)





def about():
    root.destroy()
    aboutus()


def aboutus():
    abhi=Tk()
    abhi.title('About Us')
    b3=PhotoImage(file="abboutussss.gif")
    bl3=Label(abhi,image=b3)
    bl3.grid(row=200,columns=12)
    abhi.geometry("500x500")
    
    abhi.mainloop()
    


Button(root,text="About Us", command = about,bg="#e84c3d",fg="white").grid(row=192,column=11)





root.mainloop()
