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
    if os.path.isfile(name_file):
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
            
            
    else:
        date = str(datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
        data = [{"id": 1, "description": description, "status": "todo", 
                           "createAt": date, "updateAt": date}]
        write_file(name_file, data)
        print("Task added successfully (ID: 1)")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="test task tracker for learn")
    parser.add_argument("-a", "-add", help="Введите описание задачи которую вы хотите создать", dest="create")
    argv = parser.parse_args()
    if argv.create is not None:
        create_task(argv.create)