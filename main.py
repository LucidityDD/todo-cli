import json

def list():
    with open("tasks.json", "r") as tasks:
        tasklist = json.load(tasks)
        for task in tasklist:
            print(task["description"])

def main():
    list()

main()
