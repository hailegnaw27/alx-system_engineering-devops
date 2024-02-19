#!/usr/bin/python3
"""
This script exports to-do list information for a given employee ID to JSON format.
It utilizes the JSONPlaceholder API to retrieve the necessary data.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from command line arguments
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user data based on the employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")  # Get the username of the employee

    # Retrieve the to-do list of the employee
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Create a JSON object with the required information
    data = {
        user_id: [
            {
                "task": t.get("title"),  # Retrieve the title of each task
                "completed": t.get("completed"),  # Check if the task is completed or not
                "username": username  # Include the username in each task
            } for t in todos
        ]
    }

    # Write the data to a JSON file named after the user ID
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile)

    print("Task information exported to JSON successfully.")
