class Student:
	def __init__(self, Name, Age):
		self.name = Name
		self.age = Age
		self.subjects = []
		
	def __str__(self):
		return f'Student: {self.name}\nAge: {self.age}\nSubjects: {self.subjects}'
		
	def enroll(self, subject):
		self.subjects.append(subject)
		
		
Kevin = Student("Kevin", 15)
Kevin.enroll("English")
Kevin.enroll("Geography")
Kevin.enroll("Chemistry")

print(Kevin)
