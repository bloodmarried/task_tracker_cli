import json
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