import argparse
import json

parser = argparse.ArgumentParser(description="test task tracker for learn")
parser.add_argument("add", help="Создать новую задачу")
print(parser.parse_args())