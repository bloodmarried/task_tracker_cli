from utils.task_operation import create_task, view_tasks, update_task, delete_task, mark_progress, mark_done
from utils.design import text_help

import os
import argparse


def app_run():

    parser = argparse.ArgumentParser(description="test task tracker for learn")
    parser.add_argument("pos", help=text_help(), nargs="+")

    argv = parser.parse_args()
    name_file = "db.json"
    if not os.path.isfile(name_file):
        with open(name_file, "w"):
            pass
    if argv.pos[0] == "add":
        if len(argv.pos) != 2:
            print("Неверное количество аргументов")
            return
        create_task(name_file, argv.pos[1])
    elif argv.pos[0] == "list":
        if len(argv.pos) > 2:
            print("Неверное количество аргументов")
        elif len(argv.pos) == 2:
            if argv.pos[1] in ["todo", "in-progress", "done"]:
                view_tasks(name_file, argv.pos[1])
            else:
                print("Введенный вами статус неккоректный (доступны todo, in-progress, done)")
        elif len(argv.pos) == 1:
            view_tasks(name_file, None)
    elif argv.pos[0] == "update":
        if len(argv.pos) == 3:
            *other, task_id, description = argv.pos
            if task_id.isdigit():
                task_id = int(task_id)
                update_task(name_file, task_id, description)
            else:
                print("Введите первым аргументом число")
        else:
            print("Неправильное количество аргументов")
    if argv.pos[0] == "delete":
        if len(argv.pos) == 2:
            if argv.pos[1].isdigit():
                i = int(argv.pos[1])
                delete_task(name_file, i)
            else:
                print("Введите число")
        else:
            print("Неккоректное количество аргументов")
    if argv.pos[0] == "mark-in-progress":
        if len(argv.pos) == 2:
            if argv.pos[1].isdigit():
                i = int(argv.pos[1])
                mark_progress(name_file, i)
            else:
                print("Введите число")
        else:
            print("Неккоректное число аргументов")
    if argv.pos[0] == "mark-done":
        if len(argv.pos) == 2:
            if argv.pos[1].isdigit():
                i = int(argv.pos[1])
                mark_done(name_file, i)
            else:
                print("Введите число")
        else:
            print("Неккоректное число аргументов")