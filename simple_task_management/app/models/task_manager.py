from models.task import Task
from typing import Self, Any

class TaskManager:
    def __init__(self: Self):
        self._tasks: dict[str, Task] = {}
    
    @property
    def tasks(self: Self) -> dict[str, Task]:
        return self._tasks
    
    @tasks.setter
    def tasks(self: Self, value: Any) -> None:
        if type(self._tasks) == dict:
            raise AttributeError("You can't directly assign value to " +
                                 "`tasks`, use `add_task` method to create " +
                                 "new task")
        
    def add_task(self: Self, title: str, description: str) -> int:
        new_task: Task = Task(title, description)
        self._tasks[str(new_task.id)] = new_task
        return new_task.id
    
    def remove_task(self: Self, id: int) -> None:
        del self.tasks[id]
    
    def mark_task_completed(self: Self, id: int) -> None:
        self.tasks[id].mark_as_completed()
    
    def list_tasks(self: Self) -> None:
        for task in self.tasks.values():
            print(f'id: {task.id}')
            print(f'title: {task.title}')
            print(f'status: {'Completed' if task.completed else 'Not completed'}')
            print('===============\n')

    def find_task(self: Self, id: int) -> Task:
        try:
            task = self.tasks[str(id)]
            return task
        except KeyError:
            return None      
