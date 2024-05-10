from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from classStudent import Student

root = Tk()
root.geometry("500x500")
root.title("Cadastro")

fullName = Label(root,text="Full name: ")
fullName.grid(column=0, row=0)
fullNameEntrada = Entry(root)
fullNameEntrada.grid(column=1, row=0)

calendar = Label(root, text="Birth date") 
calendar.grid(column=0, row=3)
birthDateEntry = DateEntry(root, width=12,background='darkblue', foreground='white', borderwidth=2)
birthDateEntry.grid(column=1, row=3)


def onClickGetMatricula():
    Student.getStudents()  

def onClickCadastro():
    student = Student(fullNameEntrada.get(), birthDateEntry.get_date().strftime("%m/%d/%Y").replace("-", "/"))
    #student.createTable()
    student.insertStudent()
    messagebox.showinfo("Retorno", f'Successfully registered, {fullNameEntrada.get()}')
    """ try:
        
    except:
        messagebox.showerror("Error", f'Unable to register') """
    
    
    
    
botaoSair = Button(root, text="Sair", command=root.destroy)
botaoSair.grid(column=0, row=4)
botaoEnviar = Button(root, text="Cadastrar", command=onClickCadastro)
botaoEnviar.grid(column=1, row=4)
botaoMatricula = Button(root, text="Pesquisar alunos", command = onClickGetMatricula)
botaoMatricula.grid(column=2, row=4)

root.mainloop()