#!/usr/bin/python3
"""
This script exports to-do list information of all employees to JSON format.
It utilizes the JSONPlaceholder API to retrieve the necessary data.
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve data for all employees
    users = requests.get(url + "users").json()

    # Create a JSON object with the required information for each employee
    data = {
        u.get("id"): [
            {
                "task": t.get("title"),  # Retrieve the title of each task
                "completed": t.get("completed"),  # Check if the task is completed or not
                "username": u.get("username")  # Include the username in each task
            } for t in requests.get(url + "todos", params={"userId": u.get("id")}).json()
        ]
        for u in users
    }

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)

    print("Task information of all employees exported to JSON successfully.")
