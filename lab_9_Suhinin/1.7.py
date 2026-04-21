import string
import random
def generate_password(length):
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(length))
    print(password)
generate_password(8)