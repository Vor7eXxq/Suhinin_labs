class Person:
  def __init__(self,name,age):
    self.name = name
    self.__age = age
  @property
  def age(self):
    return self.__age
  @age.setter
  def age(self,value):
    if value<0 or value >120:
      raise ValueError()
    else:
      self.__age = value
man = Person("Ivan",21)
man.age = 121
print(man.age)