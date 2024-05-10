from tkinter import *
from tkinter import messagebox
from classStudent import Student






root = Tk()
root.geometry("500x500")
root.title("Cadastro")

primeiroNome = Label(root,text="Primeiro nome: ")
primeiroNome.grid(column=0, row=0)
primeiroNomeEntrada = Entry(root)
primeiroNomeEntrada.grid(column=1, row=0)

lblIdade=Label(root, text="Idade: ")
idadeEntrada = Entry(root)
lblIdade.grid(column=0, row=3)
idadeEntrada.grid(column=1, row=3)

pegaMatricula=Label(root, text="Nome para recuperar a matricula: ")
pegaMatricula.grid(column=0, row=8)
matriculaEntrada = Entry(root)
matriculaEntrada.grid(column=1, row=9)


def onClickGetMatricula():
    Student.getStudents()  

def onClickCadastro():
    try:
        student = Student(primeiroNomeEntrada.get(), idadeEntrada.get())
        student.createTable()
        student.insertStudent()
        messagebox.showinfo("Retorno", f'Cadastro realizado com sucesso, {primeiroNomeEntrada.get()}')
    except:
        messagebox.showerror("Retorno", f'Não foi possível realizar o cadastro')
    
    
    
    
botaoSair = Button(root, text="Sair", command=root.destroy)
botaoSair.grid(column=0, row=4)
botaoEnviar = Button(root, text="Cadastrar", command=onClickCadastro)
botaoEnviar.grid(column=1, row=4)
botaoMatricula = Button(root, text="Matrícula", command = onClickGetMatricula)
botaoMatricula.grid(column=2, row=10)

root.mainloop()