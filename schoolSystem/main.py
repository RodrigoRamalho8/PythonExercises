from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from classStudent import Student

root = Tk()
root.geometry("500x500")
root.title("Register window")

fullName = Label(root,text="Full name: ")
fullName.place(relx = 0.4, rely=0.4,anchor=CENTER)
fullNameEntrada = Entry(root)
fullNameEntrada.place(relx = 0.6, rely=0.4,anchor=CENTER)

calendar = Label(root, text="Birth date")
calendar.place(relx = 0.4, rely=0.45,anchor=CENTER)
birthDateEntry = DateEntry(root, width=12,background='darkblue', foreground='white', borderwidth=2)
birthDateEntry.place(relx = 0.58, rely = 0.45, anchor=CENTER)


def onClickGetMatricula():
    Student.getStudents()  

def onClickCadastro():
    
    try:
        student = Student(fullNameEntrada.get(), birthDateEntry.get_date().strftime("%m/%d/%Y").replace("-", "/"))
        student.insertStudent()
        messagebox.showinfo("Retorno", f'Successfully registered, {fullNameEntrada.get()}')
    except:
        messagebox.showerror("Error", f'Unable to register')
    
    
    
    
botaoSair = Button(root, text="Exit", command=root.destroy)
botaoSair.place(relx = 0.44, rely = 0.6, anchor=CENTER)
botaoEnviar = Button(root, text="Register", command=onClickCadastro)
botaoEnviar.place(relx = 0.54, rely = 0.6, anchor=CENTER)
botaoMatricula = Button(root, text="List students", command = onClickGetMatricula)
botaoMatricula.place(relx = 0.49, rely = 0.7, anchor=CENTER)

root.mainloop()