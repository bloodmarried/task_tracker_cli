from utils.task_operation import create_task, view_tasks, update_task, delete_task

import os
import argparse


def app_run():

    parser = argparse.ArgumentParser(description="test task tracker for learn")
    parser.add_argument("-a", "-add", help="Введите описание задачи которую вы хотите создать", dest="create")
    parser.add_argument("-l", "-list", help = "Выводит список задач", dest = "list", choices = ["todo", "in-progress", "done"], nargs="?", default=False)
    parser.add_argument("-u", "-update", help="Обновить описание задачи, 1 аргументом передается id, вторым описание", dest="update", nargs=2, default=None)
    parser.add_argument("-d", "-delete", help="Удалить задачу", dest="delete", nargs=1, type=int)

    argv = parser.parse_args()
    name_file = "db.json"

    if not os.path.isfile(name_file):
        with open(name_file, "w"):
            pass
    if argv.create is not None:
        create_task(name_file, argv.create)
    if argv.list is not False:
        view_tasks(name_file, argv.list)
    if argv.update is not None:
        task_id, description = argv.update
        if task_id.isdigit():
            task_id = int(task_id)
            update_task(name_file, task_id, description)
        else:
            print("Введите первым аргументом число")
    if argv.delete is not None:
        delete_task(name_file, *argv.delete)