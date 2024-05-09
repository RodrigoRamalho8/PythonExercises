import sqlite3
studentsList = []
class Student():
    
    def __init__(self, nome, idade):
        self.matricula = -1
        self.nome = nome
        self.idade = idade        
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()


    def createTable(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
        matricula INTEGER PRIMARY KEY,
        nome VARCHAR(32),
        idade INTEGER
        )
        """)
        self.connection.commit()  



    def insertStudent(self):              
        self.cursor.execute("""
        INSERT INTO students VALUES
        (NULL,'{}',{})
        """.format(self.nome, self.idade))
        self.connection.commit()
        self.connection.close()
        studentsList.append(Student.matricula.value())          

    def getMatricula(self):
        if self.matricula < 1:
            self.cursor.execute("""
            SELECT matricula FROM students
            WHERE nome = {}
            """).format(self.nome)
            result =self.cursor.fetchone()
            for i in result:
                print(i)
            self.matricula = result[0]
        
        return self.matricula
    