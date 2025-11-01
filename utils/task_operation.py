from utils.json_operation import read_file, write_file
import datetime
from utils.design import pretty_table


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
    if tasks is not None and tasks:
        delete_ok = False
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                delete_ok = True
                break
        if delete_ok:
            write_file(filename, tasks)
            print("Запись успешно удалена!")
        else:
            print("Запись не найдена")
    else:
        print("Файл пуст!")
        

def update_task(filename: str, task_id: int, new_description: str):
    tasks: list[dict] | None = read_file(filename)
    if tasks is not None and tasks:
        update_ok = False
        
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                date = str(datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
                task["updateAt"] = date
                update_ok = True
                break

        if update_ok:
            write_file(filename, tasks)
            print("Задача успешно изменена!")
        else:
            print("Такой задачи не существует")
    else:
        print("Файл пуст")


def create_task(name_file: str, description: str):

    tasks: list[dict] | None = read_file(name_file)
    date = str(datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
    if tasks is not None and tasks:
        last_task = tasks[-1]
        new_id = last_task["id"] + 1
        data = {"id": new_id, "status": "todo", "description": description, 
                "createAt": date, "updateAt": date}
        tasks.append(data)
        write_file(name_file, tasks)
        print(f"Task added successfully (ID: {new_id})")
    else:
        
        data = [{"id": 1, "status": "todo", "description": description, 
                        "createAt": date, "updateAt": date}]
        write_file(name_file, data)
        print("Task added successfully (ID: 1)")
            

def view_tasks(name_file: str, flag: str):
    tasks: list[dict] | None = read_file(name_file)
    if tasks is None:
        print("No tasks")
    elif flag is None:
        text = ["id", "Status", "Description", "Time create", "Time Update"]
        
        array = [text]
        for task in tasks:
            task = list(task.values())
            array.append(task)
            print(task)
        print(pretty_table(array)) 
    else:
        text = ["id", "Description", "Time create", "Time Update"]
        array = [text]
        for task in tasks:
            if task["status"] == flag:
                ar = [task["id"], task["description"], task["createAt"], task["updateAt"]]
                array.append(ar)

        print(pretty_table(array))