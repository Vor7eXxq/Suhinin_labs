import datetime
def show_datetime():
    now = datetime.datetime.now()
    print(now.strftime(f"Сьогодні: %d.%m.%Y, час: %H:%M "))
show_datetime()