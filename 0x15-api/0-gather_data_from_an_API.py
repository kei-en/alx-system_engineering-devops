#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    jso_n = res.json()
    print("Employee {} is done with tasks".format(jso_n.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    tsk = []
    for task in tasks:
        if task.get('completed') is True:
            tsk.append(task)

    print("({}/{}):".format(len(tsk), len(tasks)))
    for task in tsk:
        print("\t {}".format(task.get("title")))
