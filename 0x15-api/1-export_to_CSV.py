#!/usr/bin/python3

import csv
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))

            with open(f'{id}.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                for todo in todos:
                    writer.writerow([id, user_name, todo.get('completed'), todo.get('title')])
