class Animal:
  def __init__(self,name,species):
    self.name = name
    self.species = species
  def get_info(self):
    print(f"{self.name} - {self.species}")
  def make_sound(self):
    print("qwerty")
class Dog(Animal):
  def __init__(self,name,species):
    super().__init__(name,species)
  def make_sound(self):
     print("Woof Woof")
dog1 = Dog("Rex","pes domashniy")
dog1.get_info()
dog1.make_sound()

