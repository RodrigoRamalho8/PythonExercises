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

    def getStudents():
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM students
        """)
        rows = cursor.fetchall()
        for i in rows:
            print(f'ID: {i[0]}\nName: {i[1]}\nAge: {i[2]} ')
        connection.commit()
        connection.close()


    def insertStudent(self):              
        self.cursor.execute("""
        INSERT INTO students (nome, idade)
        VALUES ('{}',{})
        """.format(self.nome, self.idade))
        #A partir daqui
        # sql =  "INSERT INTO students (nome) VALUES (%s)"
        # values = (self.nome)
        # print(values)
        # self.cursor.execute(sql, values)
        self.connection.commit()
        self.connection.close()
        #studentsList.append(Student.matricula.value())          

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
    