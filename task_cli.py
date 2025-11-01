import argparse
import json
import datetime
import os


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        file.seek(0)
        if os.path.getsize(file_name) > 0:
            return json.load(file)
        return None


def write_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def create_task(description):
    name_file = "db.json"
    file = read_file(name_file)
    if file is not None:
        tasks: list = file
        last_task = tasks[-1]
        date = str(datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
        new_id = last_task["id"] + 1
        data = {"id": new_id, "description": description, "status": "todo", 
                "createAt": date, "updateAt": date}
        tasks.append(data)
        write_file(name_file, tasks)
        print(f"Task added successfully (ID: {new_id})")
    else:
        date = str(datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
        data = [{"id": 1, "description": description, "status": "todo", 
                        "createAt": date, "updateAt": date}]
        write_file(name_file, data)
        print("Task added successfully (ID: 1)")
            

def view_tasks(name_file, flag):
    tasks = read_file(name_file)
    if tasks is None:
        print("No tasks")
    elif flag is None:
        text = "|     Status     |      id      |    Description    |         Time create            |    Time Update       |\n"
        for i in tasks:
            text += f"|      {i["status"]}      |      {i["id"]}       |       {i["description"]}        |      {i["createAt"]}       |       {i["updateAt"]}       |\n"
        print(text)
    else:
        text = "id      |    Description    |    Time create    |    Time Update       |\n"
        for i in tasks:
            if i["status"] == flag:
                text += f"{i["id"]}       |       {i["description"]}        |      {i["createAt"]}       |       {i["updateAt"]}       |\n"
        print(text)
        

def main():

    parser = argparse.ArgumentParser(description="test task tracker for learn")
    parser.add_argument("-a", "-add", help="Введите описание задачи которую вы хотите создать", dest="create")
    parser.add_argument("-l", "-list", help = "Выводит список задач", dest = "list", choices = ["todo", "in-progress", "done"], nargs="?", default=False)
    parser.add_argument("-u", "-update", help="Обновить описание задачи, 1 аргумент", dest="update", nargs=2, default=None)

    argv = parser.parse_args()
    name_file = "db.json"

    if not os.path.isfile(name_file):
        with open(name_file, "w"):
            pass
    if argv.create is not None:
        create_task(argv.create)
    if argv.list is not False:
        view_tasks(name_file, argv.list)
    if argv.update is not None:
        print(argv.update)


if __name__ == "__main__":
    main()
    