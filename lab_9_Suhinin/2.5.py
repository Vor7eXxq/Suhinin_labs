def add_task(task_list,task_name,priority="medium"):
    newtask = {
        "name" : task_name,
        "priority" : priority,
        "completed" : False
    }
    task_list.append(newtask)
def complete_task(task_list,task_name):
    for task in task_list:
        if task["name"] == task_name:
            task["completed"] = True
            break
tasks = []
add_task(tasks, "Вивчити Пайтон", "high")
add_task(tasks, "Купити молоко")
complete_task(tasks, "Купити молоко")
print(tasks)