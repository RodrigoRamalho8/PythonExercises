from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from classStudent import Student

root = Tk()
root.geometry("500x500")
root.title("Cadastro")

fullName = Label(root,text="Full name: ")
#fullName.grid(column=0, row=0)
fullName.place(relx = 0.4, rely=0.4,anchor=CENTER)
fullNameEntrada = Entry(root)
fullNameEntrada.grid(column=1, row=0)
fullNameEntrada.place(relx = 0.6, rely=0.4,anchor=CENTER)

calendar = Label(root, text="Birth date") 
calendar.grid(column=0, row=3)
calendar.place(relx = 0.4, rely=0.45,anchor=CENTER)
birthDateEntry = DateEntry(root, width=12,background='darkblue', foreground='white', borderwidth=2)
birthDateEntry.grid(column=1, row=3)
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
    
    
    
    
botaoSair = Button(root, text="Sair", command=root.destroy)
botaoSair.grid(column=0, row=4)
botaoSair.place(relx = 0.44, rely = 0.6, anchor=CENTER)
botaoEnviar = Button(root, text="Cadastrar", command=onClickCadastro)
botaoEnviar.grid(column=1, row=4)
botaoEnviar.place(relx = 0.54, rely = 0.6, anchor=CENTER)
botaoMatricula = Button(root, text="Pesquisar alunos", command = onClickGetMatricula)
botaoMatricula.grid(column=2, row=4)
botaoMatricula.place(relx = 0.49, rely = 0.7, anchor=CENTER)

root.mainloop()