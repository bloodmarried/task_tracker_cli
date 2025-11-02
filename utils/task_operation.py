from utils.json_operation import read_file, write_file
import datetime
from utils.design import pretty_table


def mark_done(filename, task_id):
    tasks: list[dict] | None = read_file(filename)

    if not tasks:
        print("Файл пуст")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "done":
                print("Задача уже выполнена")
                break
            else:
                task["status"] = "done"
                date = str(datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
                task["updateAt"] = date
                write_file(filename, tasks)
                print("Задача успешно отмечена как выполненная!")
                break
    else:
        print("Задача не найдена")



def mark_progress(filename, task_id):
    tasks: list[dict] | None = read_file(filename)
    if tasks is not None and tasks:
        mark = False
        for task in tasks:
            if task["id"] == task_id:
                if task["status"] == "in-progress":
                    print("Задача уже отмечена как в процессе")
                    return
                elif task["status"] == "done":
                    print("Задача уже выполнена")
                    return
                else:
                    task["status"] = "in-progress"
                    date = str(datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
                    task["updateAt"] = date
                    mark = True
        if mark:
            write_file(filename, tasks)
            print("Задача успешно отмечена как в процессе")
        else:
            print("Данной задачи не существует")
    else:
        print("Файл пуст")


def delete_task(filename, task_id):
    tasks: list[dict] | None = read_file(filename)
    
    if not tasks:
        print("Файл пуст")
        return
    
    low = 0
    high = len(tasks) - 1
    while low <= high:
        mid = (low + high) // 2
        if tasks[mid]["id"] > task_id:
            high = mid - 1
        elif tasks[mid]["id"] < task_id:
            low = mid + 1
        elif tasks[mid]["id"] == task_id:
            tasks.remove(tasks[mid])
            write_file(filename, tasks)
            print("Задача успешно удалена!")
            break
    else:
        print("Такой задачи не существует")
        

def update_task(filename: str, task_id: int, new_description: str):
    tasks: list[dict] | None = read_file(filename)
    
    if not tasks:
        print("Файл пуст")
        return
    
    low = 0
    high = len(tasks) - 1
    while low <= high:
        mid = (low + high) // 2
        
        if tasks[mid]["id"] > task_id:
            high = mid - 1
        elif tasks[mid]["id"] < task_id:
            low = mid + 1
        elif tasks[mid]["id"] == task_id:
            tasks[mid]["description"] = new_description
            date = str(datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
            tasks[mid]["updateAt"] = date
            write_file(filename, tasks)
            print("Задача успешно изменена!")
            break
    else:
        print(low, high)
        print("Такой задачи не существует")
    


def create_task(filename: str, description: str):

    tasks: list[dict] | None = read_file(filename)
    date = str(datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
    if tasks is not None and tasks:
        last_task = tasks[-1]
        new_id = last_task["id"] + 1
        data = {"id": new_id, "status": "todo", "description": description, 
                "createAt": date, "updateAt": date}
        tasks.append(data)
        write_file(filename, tasks)
        print(f"Task added successfully (ID: {new_id})")
    else:
        
        data = [{"id": 1, "status": "todo", "description": description, 
                        "createAt": date, "updateAt": date}]
        write_file(filename, data)
        print("Task added successfully (ID: 1)")
            

def view_tasks(filename: str, flag: str):
    tasks: list[dict] | None = read_file(filename)
    if tasks is None:
        print("No tasks")
    elif flag is None:
        text = ["id", "Status", "Description", "Time create", "Time Update"]
        
        array = [text]
        for task in tasks:
            task = list(task.values())
            array.append(task)
        print(pretty_table(array)) 
    else:
        text = ["id", "Description", "Time create", "Time Update"]
        array = [text]
        for task in tasks:
            if task["status"] == flag:
                ar = [task["id"], task["description"], task["createAt"], task["updateAt"]]
                array.append(ar)

        print(pretty_table(array))