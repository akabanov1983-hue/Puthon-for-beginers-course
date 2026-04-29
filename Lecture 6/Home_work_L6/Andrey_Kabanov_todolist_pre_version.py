
def create_task(max_id):
    auto_id = max_id + 1

    todo = input("todo:")
    completed = bool(input("completed (1 Для True, пустой ввод для False):"))
    userId = int(input("userId:"))
    priority = int(input("priority:"))

    new_task = {auto_id:{
    "todo": todo,
    "completed": completed,
    "userId": userId,
    "priority": priority,
}
}

    return new_task


def read_tasks():
    for tk, tdi in todos.items():

        print("Task id:", tk)

    for k, v in tdi.items():
        print(" ", k, ":", v)
    print("__________________________________")


def read_task(tid):
    res_task = todos.get(tid, -1)

    if res_task == -1:
        print("задача не найдена с id:", tid)
        return

    print("Task id:", tid)

    for k, v in res_task.items():
        print(" ", k, ":", v)

print("__________________________________")


def delete_task(tid):
    res_task = todos.get(tid, -1)

    if res_task == -1:
        print("задача не найдена с id:", tid)
        return

    print("Task id:", tid)
    todos.pop(tid)

    print("задача с id:", tid, "удалена.")
    print("__________________________________")


todos = {
1:{
"todo": "Do something nice for someone you care about",
"completed": False,
"userId": 152,
'priority': 5
},
2: {
"todo": "Memorize a poem",
"completed": True,
"userId": 13,
'priority': 5
},
3: {
"todo": "Watch a classic movie",
"completed": True,
"userId": 68,
'priority': 5
},
}


def main():
    print("1 - create, 2 read task by id, 3 reat all tasks, 4 delete task by id, 5 exit")
    operation = int(input("-->"))

    while operation != 5:
        if operation == 1:
            task = create_task(max(todos.keys()))
            todos.update(task)
        elif operation == 2:
            tid = int(input("Введи таск id:"))
            read_task(tid)
        elif operation == 3:
            read_tasks()
        elif operation == 4:
            tid = int(input("Введи таск id:"))
            delete_task(tid)
        else:
            print("я не понял попробуй ещё раз.")

print("1 - create, 2 read task by id, 3 reat all tasks, 4 delete task by id, 5 exit")

operation = int(input("-->"))

print("пока пока")


main()
