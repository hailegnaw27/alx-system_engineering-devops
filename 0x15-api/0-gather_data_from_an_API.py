#!/usr/bin/python3

import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            employee_id = int(sys.argv[1])
            user_response = requests.get(f'{API_URL}/users/{employee_id}').json()
            todos_response = requests.get(f'{API_URL}/todos?userId={employee_id}').json()
            employee_name = user_response.get('name')
            total_tasks = len(todos_response)
            completed_tasks = sum(task.get('completed') for task in todos_response)

            print(f'Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):')
            for task in todos_response:
                if task.get('completed'):
                    print(f'\t{task.get("title")}')
