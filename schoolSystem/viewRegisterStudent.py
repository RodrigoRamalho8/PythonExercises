from tkinter import *
import tkinter as tk
from controllerStudent import onClickCadastro, onClickGetMatricula
from tkcalendar import Calendar, DateEntry

class viewRegisterStudent:

    root = Tk()
    root.geometry("500x500")
    root.title("Register window")
    root.configure(background='gray')

    firstName = Label(root,text="First name: ", font = ("Copperplate Gothic Light", 10), background="gray")
    firstName.place(relx = 0.35, rely=0.3,anchor=CENTER)
    firstNameEntry = Entry(root)
    firstNameEntry.place(relx = 0.61, rely=0.3,anchor=CENTER)

    lastName = Label(root,text="Last name: ", font = ("Copperplate Gothic Light", 10), background="gray")
    lastName.place(relx = 0.35, rely=0.38,anchor=CENTER)
    lastNameEntry = Entry(root)
    lastNameEntry.place(relx = 0.61, rely=0.38,anchor=CENTER)

    calendar = Label(root, text="Birth date",font = ("Copperplate Gothic Light", 10), background="gray")
    calendar.place(relx = 0.4, rely=0.45,anchor=CENTER)
    birthDateEntry = DateEntry(root, width=12,background='darkblue', foreground='white', borderwidth=2,font = ("Copperplate Gothic Light", 10),date_pattern='mm/dd/yyyy')
    birthDateEntry.place(relx = 0.61, rely = 0.45, width="126",anchor=CENTER)

    botaoSair = Button(root, text="Exit",font = ("Copperplate Gothic Light", 10),compound=tk.LEFT,command=root.destroy)
    botaoSair.place(relx = 0.35, rely = 0.6, anchor=CENTER)
    botaoMatricula = Button(root, text="List students",font = ("Copperplate Gothic Light", 10), command=onClickGetMatricula)
    botaoMatricula.place(relx = 0.5, rely = 0.6, anchor=CENTER)
    botaoEnviar = Button(root, text="Register",font = ("Copperplate Gothic Light", 10), command=onClickCadastro(firstNameEntry.get(), lastNameEntry.get(), birthDateEntry.get_date().strftime("%m/%d/%Y").replace("-", "/")))
    botaoEnviar.place(relx = 0.685, rely = 0.6, anchor=CENTER)


    root.mainloop()