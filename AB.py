#Ayushi Patel
#Address Book

#Imported Tkinter from library to use for buttons
#Imported Database to use for importing data of users.
import sys
sys.path.insert(0, 'GUI')
from tkinter import *
from databases import Database

#Its for font style, and font size for the display windowss and text.
top = Tk()
top.geometry('1000x600')
top.config(bg = 'grey')
top.resizable(0,0)
top.title('AddressBook')

#To display some of the users in the address book
addressBook = [
    ['Ayushi Patel',  '123456788', '123 Thomas Street', '3/30/98', 'pateayus@kean.edu'],
]

Name = StringVar()
Number = StringVar()
Address = StringVar()
BirthDate = StringVar()
Email = StringVar()

frame = Frame(top)
frame.pack(side = RIGHT)

#This is a display box font 
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, width=50,height=25)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

#All the method and functions going to defined here
def Selected():
    return int(select.curselection()[0])

def ADD():
    addressBook.append([Name.get(), Number.get(), Address.get(), BirthDate.get(), Email.get()])
    Select_set()

def EDIT():
    addressBook[Selected()] = [Name.get(), Number.get(), Address.get(), BirthDate.get(), Email.get()]
    Select_set()


def DELETE():
    del addressBook[Selected()]
    Select_set()

def VIEW():
    NAME, PHONE, ADDRESS, BIRTHDATE, EMAIL = addressBook[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Address.set(ADDRESS)
    BirthDate.set(BIRTHDATE)
    Email.set(EMAIL)

def EXIT():
    top.destroy()

def RESET():
    Name.set('')
    Number.set('')
    Address.set('')
    BirthDate.set('')
    Email.set('')

def Select_set() :
    addressBook.sort()
    select.delete(0,END)
    for name,phone,address,birthdate,email in addressBook :
        select.insert (END, name)
Select_set()

#Buttons and Labels will be used when they want to click on category instead of writing it out
#I also added an Entry box for users to add data.
Label(top, text = 'Name: ', font='arial 12 bold', bg = 'SlateGray3').place(x= 30, y=20)
Entry(top, textvariable = Name).place(x= 100, y=20)

Label(top, text = 'Ph.No: ', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=60)
Entry(top, textvariable = Number).place(x= 120, y=60)

Label(top, text = 'Address: ', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=100)
Entry(top, textvariable = Address).place(x= 130, y=100)

Label(top, text = 'Birthdate: ', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=140)
Entry(top, textvariable = BirthDate).place(x= 140, y=140)

Label(top, text = 'Email: ', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=180)
Entry(top, textvariable = Email).place(x= 150, y=180)

A=Button(top,text="EXIT", font='arial 12 bold',bg='grey', command = EXIT, width=12)
A.place(relx=0.5, rely=0.35, anchor=CENTER)

B=Button(top,text="ADD", font='arial 12 bold',bg='grey',command = ADD,width=12)
B.place(relx=0.5, rely=0.10, anchor=CENTER)

C=Button(top,text="EDIT", font='arial 12 bold',bg='grey',command = EDIT,width=12)
C.place(relx=0.5, rely=0.15, anchor=CENTER)

D=Button(top,text="VIEW", font='arial 12 bold',bg='grey', command = VIEW,width=12)
D.place(relx=0.5,rely=0.20,  anchor=CENTER)

E=Button(top,text="DELETE", font='arial 12 bold',bg='grey', command = DELETE,width=12)
E.place(relx=0.5, rely=0.25, anchor=CENTER)

F=Button(top,text="RESET", font='arial 12 bold',bg='grey', command = RESET,width=12)
F.place(relx=0.5, rely=0.30, anchor=CENTER)

#Final statement for program to know it ready to run
top.mainloop()