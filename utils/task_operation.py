from utils.json_operation import read_file, write_file
import datetime


def update_task(filename: str, task_id: int, new_description: str):
    tasks: list[dict] | None = read_file(filename)
    if tasks is not None:
        update_ok = False
        
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
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
    if tasks is not None:
        last_task = tasks[-1]
        new_id = last_task["id"] + 1
        data = {"id": new_id, "description": description, "status": "todo", 
                "createAt": date, "updateAt": date}
        tasks.append(data)
        write_file(name_file, tasks)
        print(f"Task added successfully (ID: {new_id})")
    else:
        
        data = [{"id": 1, "description": description, "status": "todo", 
                        "createAt": date, "updateAt": date}]
        write_file(name_file, data)
        print("Task added successfully (ID: 1)")
            

def view_tasks(name_file: str, flag: str):
    tasks: list[dict] | None = read_file(name_file)
    if tasks is None:
        print("No tasks")
    elif flag is None:
        text = "|     Status     |      id      |    Description    |         Time create            |    Time Update       |\n"
        for i in task:
            text += f"|      {i["status"]}      |      {i["id"]}       |       {i["description"]}        |      {i["createAt"]}       |       {i["updateAt"]}       |\n"
        print(text)
    else:
        text = "id      |    Description    |    Time create    |    Time Update       |\n"
        for i in tasks:
            if i["status"] == flag:
                text += f"{i["id"]}       |       {i["description"]}        |      {i["createAt"]}       |       {i["updateAt"]}       |\n"
        print(text)