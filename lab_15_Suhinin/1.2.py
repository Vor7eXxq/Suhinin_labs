class Student:
  def __init__(self,name,id):
    self.name = name
    self.id = id
class Extended_Student(Student):
  def __init__(self,name,id,speciality):
    self.speciality = speciality
    super().__init__(name,id)
  def display_info(self):
    print(f"Студент: {self.name}, ID: {self.id}, Спеціальність: {self.speciality}")
s = Extended_Student("Коля","12345", "Кн")
s.display_info()