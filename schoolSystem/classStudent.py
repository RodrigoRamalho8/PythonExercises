import sqlite3
from datetime import date
class Student():
    
    def __init__(self, fname, lname, birthdate):
        self.validateNames(fname, lname)
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.age = self.getAge()
        self.registerDate = str(date.today().strftime("%m/%d/%Y").replace("-", "/"))      
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()
        self.createTable()

           


    def createTable(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        fname VARCHAR(32),
        lname VARCHAR(32),
        birthdate TEXT,
        registerDate TEXT
        )
        """)
        self.connection.commit()  

    def getStudents(self):
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM students
        """)
        rows = cursor.fetchall()
        for i in rows:
            print(f'ID: {i[0]}\nName: {i[1]} {i[2]}\nAge: {self.getAge()}\nBirthdate: {i[3]}\nRegister date: {i[4]} ')
        connection.commit()
        connection.close()


    def insertStudent(self):
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO students (fname,lname, birthdate, registerDate)
        VALUES ('{}','{}','{}','{}')
        """.format(self.fname, self.lname, self.birthdate, self.registerDate))
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
    
    def getAge(self):
        today = date.today()
        birthyear = self.birthdate.split()
        self.age = today.year - int(birthyear[0][6:])
        return self.age
    
    def validateNames(self,fname, lname): 
        if not self.fname.isalpha() or not self.lname.isalpha():
            raise Exception("Name invalid!")
    
    # def setName(self,fname,lname):
    #     self.validateNames(fname, lname)
    #     self.fname = fname
    #     self.lname = lname
        
    
    


    