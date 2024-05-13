import sqlite3
from datetime import date
class Student():
    
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        self.age = self.getAge()
        self.registerDate = str(date.today().strftime("%m/%d/%Y").replace("-", "/"))      
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()
        self.createTable()

    def getAge(self):
        today = date.today()
        birthyear = self.birthdate.split()
        self.age = today.year - int(birthyear[0][6:])
        return self.age
        


    def createTable(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name VARCHAR(32),
        age INTEGER,
        birthdate TEXT,
        registerDate TEXT
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
            print(f'ID: {i[0]}\nName: {i[1]}\nAge: {i[2]}\nBirthdate: {i[3]}\nRegister date: {i[4]} ')
        connection.commit()
        connection.close()


    def insertStudent(self):
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO students (name, age, birthdate, registerDate)
        VALUES ('{}',{},'{}','{}')
        """.format(self.name, self.age, self.birthdate, self.registerDate))
        connection.commit()
        connection.close()          

    def getMatricula(self):
        if self.matricula < 1:
            self.cursor.execute("""
            SELECT id FROM students
            WHERE nome = {}
            """).format(self.name)
            result =self.cursor.fetchone()
            for i in result:
                print(i)
            self.id = result[0]
        
        return self.id
    