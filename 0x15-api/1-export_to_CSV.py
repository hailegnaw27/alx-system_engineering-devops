#!/usr/bin/python3
'''A script that gathers data from an external API and exports it to a CSV file.'''
import csv
import re
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'
'''The URL of the external API.'''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])
            # Fetch user details from the API
            user_response = requests.get(f'{API_URL}/users/{employee_id}').json()
            # Fetch tasks for the user from the API
            todos_response = requests.get(f'{API_URL}/todos?userId={employee_id}').json()
            employee_name = user_response.get('username')

            with open(f'{employee_id}.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                # Write each task as a row in the CSV file
                for task in todos_response:
                    writer.writerow([employee_id, employee_name, task.get('completed'), task.get('title')])
