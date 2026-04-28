import datetime
from calculator import Calculator
print(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {Calculator.add(5,3)}")
print(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {Calculator.divide(4,2)}")
print(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {Calculator.multiply(10,2)}")