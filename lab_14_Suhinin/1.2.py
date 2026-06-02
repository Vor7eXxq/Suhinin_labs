class Book:
  def __init__(self,author,title):
    self.author = author
    self.title = title
  def get_info(self):
    print(f"Назва: {self.title}, Автор: {self.author}")
book = Book("George Orwell", "1984")
book.get_info()