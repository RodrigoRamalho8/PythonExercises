from tkinter import messagebox
from classStudent import Student
from viewRegisterStudent import *

class controllerStudent:
    def onClickGetMatricula():
        Student.getStudents()  

    def onClickCadastro():
            try:
                student = Student(fname,lname,birthdate)
                student.insertStudent()
                messagebox.showinfo("Retorno", f'Successfully registered, {fname}')
            except Exception as e:
                messagebox.showerror("Error", f'{e}')


  

        
    