from models.task import Task
from typing import Self, Any

class TaskManager:
    def __init__(self: Self):
        self._tasks: list[Task] = []
    
    @property
    def tasks(self: Self) -> list[Task]:
        return self._tasks
    
    @tasks.setter
    def tasks(self: Self, value: Any) -> None:
        if type(self._tasks) == list:
            raise AttributeError("You can't directly assign value to " +
                                 "`tasks`, use `add_task` method to create " +
                                 "new task")
        
    def add_task(self: Self, title: str, description: str) -> int:
        new_task: Task = Task(title, description)
        self._tasks.append(new_task)
        return new_task.id
    
    def show_tasks(self: Self) -> list[Task]:
        return self.tasks
        

