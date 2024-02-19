#!/usr/bin/python3

import requests
from sys import argv


def gather_data(employee_id):
    """
    Gathers data from the API for a given employee ID
    and displays the employee's TODO list progress.
    """
    # Make a GET request to fetch employee information
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Make a GET request to fetch employee's TODO list
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Calculate the number of completed tasks and total tasks
    total_tasks = len(todo_data)
    completed_tasks = sum(task.get('completed') for task in todo_data)

    # Print the employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

    # Print the titles of completed tasks
    for task in todo_data:
        if task.get('completed'):
            print("\t{}".format(task.get('title')))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    gather_data(employee_id)
