from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from classStudent import Student

root = Tk()
root.geometry("500x500")
root.title("Register window")
root.configure(background='gray')

fullName = Label(root,text="Full name: ", font = ("Copperplate Gothic Light", 10), background="gray")
fullName.place(relx = 0.4, rely=0.4,anchor=CENTER)
fullNameEntrada = Entry(root)
fullNameEntrada.place(relx = 0.61, rely=0.4,anchor=CENTER)

calendar = Label(root, text="Birth date",font = ("Copperplate Gothic Light", 10), background="gray")
calendar.place(relx = 0.4, rely=0.45,anchor=CENTER)
birthDateEntry = DateEntry(root, width=12,background='darkblue', foreground='white', borderwidth=2,font = ("Copperplate Gothic Light", 10) )
birthDateEntry.place(relx = 0.61, rely = 0.45, width="126",anchor=CENTER)


def onClickGetMatricula():
    Student.getStudents()  

def onClickCadastro():
    
    try:
        student = Student(fullNameEntrada.get(), birthDateEntry.get_date().strftime("%m/%d/%Y").replace("-", "/"))
        student.insertStudent()
        messagebox.showinfo("Retorno", f'Successfully registered, {fullNameEntrada.get()}')
    except:
        messagebox.showerror("Error", f'Unable to register')
    
    
  
botaoSair = Button(root, text="Exit",font = ("Copperplate Gothic Light", 10),compound=tk.LEFT,command=root.destroy)
botaoSair.place(relx = 0.35, rely = 0.6, anchor=CENTER)
botaoMatricula = Button(root, text="List students",font = ("Copperplate Gothic Light", 10), command = onClickGetMatricula)
botaoMatricula.place(relx = 0.5, rely = 0.6, anchor=CENTER)
botaoEnviar = Button(root, text="Register",font = ("Copperplate Gothic Light", 10), command=onClickCadastro)
botaoEnviar.place(relx = 0.685, rely = 0.6, anchor=CENTER)

root.mainloop()