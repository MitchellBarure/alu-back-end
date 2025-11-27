#!/usr/bin/python3
"""
Exports all employees' To Do list data to JSON format.
"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all the users
    users = requests.get(f"{base_url}/users").json()

    # Create a dictionary to store all users' tasks
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Get to dos for this user
        todos_url = f"{base_url}/todos"
        todos = requests.get(todos_url, params={"userId": user_id}).json()

        all_tasks[user_id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos
        ]

    # Write the data to file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
