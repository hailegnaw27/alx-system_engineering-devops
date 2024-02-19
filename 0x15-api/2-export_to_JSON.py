#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(user_id))  # Get user data
    todos_response = requests.get(url + "todos", params={"userId": user_id})  # Get to-do tasks for the user

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user = user_response.json()  # Convert user response to JSON
        todos = todos_response.json()  # Convert to-do tasks response to JSON
        username = user.get("username")  # Get the username from the user data

        data = {
            "user_id": user_id,
            "username": username,
            "todos": todos
        }

        with open("{}.json".format(user_id), "w") as jsonfile:
            json.dump(data, jsonfile)  # Save the data as JSON

        print("Task information exported to JSON successfully.")
    else:
        print("Failed to retrieve data from JSONPlaceholder API. Please check the user ID.")
