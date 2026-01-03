class Todo:
    next_id = 1

    def __init__(self, title, description=""):
        self.id = Todo.next_id
        Todo.next_id += 1
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}, Status: {status}"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }