class PasswordManager:
  def __init__(self,password):
    self.__password = password
  @property
  def password(self):
    return self.__password
  @password.setter
  def password(self,newpassword):
    if len(newpassword) < 8 or not any(char.isdigit() for char in newpassword):
      raise ValueError("Пароль повинен мати хоча б 8 символів та одну цифру")
    else:
      self.__password = newpassword

p=PasswordManager("")
p.password = "qwertyz2xc"
print(p.password)
