import json
import os
from todo import Todo
from rich.console import Console

class TodoManager:
    def __init__(self, data_file="todos.json"):
        self.data_file = data_file
        self.todos = []
        self.load_from_file()

    def save_to_file(self):
        """Save todos to a JSON file"""
        try:
            # Prepare data for serialization
            data = []
            for todo in self.todos:
                # Store the next_id to maintain ID sequence
                data.append({
                    "id": todo.id,
                    "title": todo.title,
                    "description": todo.description,
                    "completed": todo.completed
                })

            # Save to file
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self):
        """Load todos from a JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                self.todos = []
                max_id = 0
                for item in data:
                    todo = Todo(item["title"], item["description"])
                    # Override the auto-generated ID with the saved ID
                    todo.id = item["id"]
                    todo.completed = item["completed"]
                    self.todos.append(todo)
                    if todo.id > max_id:
                        max_id = todo.id

                # Set the next_id to continue from the highest ID
                Todo.next_id = max_id + 1
            except Exception as e:
                print(f"Error loading from file: {e}")
                self.todos = []
        else:
            # If no file exists, initialize with empty list
            self.todos = []

    def add_todo(self, title, description=""):
        todo = Todo(title, description)
        self.todos.append(todo)
        self.save_to_file()  # Save after adding
        return todo

    def get_all_todos(self):
        return self.todos

    def find_todo_by_id(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id, new_title=None, new_description=None):
        todo = self.find_todo_by_id(todo_id)
        if todo:
            if new_title is not None:
                todo.title = new_title
            if new_description is not None:
                todo.description = new_description
            self.save_to_file()  # Save after updating
            return True
        return False

    def delete_todo(self, todo_id):
        todo = self.find_todo_by_id(todo_id)
        if todo:
            self.todos.remove(todo)
            self.save_to_file()  # Save after deleting
            return True
        return False

    def toggle_complete(self, todo_id):
        todo = self.find_todo_by_id(todo_id)
        if todo:
            todo.completed = not todo.completed
            self.save_to_file()  # Save after toggling
            return True
        return False