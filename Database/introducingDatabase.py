import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()
sql_query = "SELECT name FROM sqlite_master"
cursor.execute(sql_query)
print(cursor.fetchall())
res = cursor.execute("CREATE TABLE IF NOT EXISTS student(name TEXT, age INTEGER, subjects list<varchar>)")

class Student:
	def __init__(self, Name, Age):
		self.name = Name
		self.age = Age
		self.subjects = []
		
		
	def __str__(self):
		return f'Student: {self.name}\nAge: {self.age}\nSubjects: {self.subjects}'
		
	def enroll(self, subject):
		self.subjects.append(subject)

	def add_Student_To_Database(connection, Student):
		sql = """INSERT INTO students(name, age)
			  	 VALUES(?,?)"""
		cursor.execute(sql, Student)
		connection.commit()
		return cursor.lastrowid
		
Kevin = Student("Kevin", 15)
Kevin.enroll("English")
Kevin.enroll("Geography")
Kevin.enroll("Chemistry")
Kevin.add_Student_To_Database(Kevin)
#print(connection.total_changes())
print(Kevin)
