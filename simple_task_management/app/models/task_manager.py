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
        from models import storage

        new_task: Task = Task(title, description)
        storage.new(new_task)
        storage.save()
        return new_task.id
    
    def remove_task(self: Self, id: int) -> None:
        from models import storage

        storage.delete(id)
        storage.save()
    
    def mark_task_completed(self: Self, id: int) -> None:
        from models import storage

        tasks: dict[str, Task] = storage.all()
        tasks[id].mark_as_completed()

        storage.save()
    
    def list_tasks(self: Self) -> None:
        from models import storage

        for task in storage.all().values():
            print(f'id: {task.id}')
            print(f'title: {task.title}')
            print(f'description: {task.description}')
            print(f'status: {'Completed' if task.completed else 'Not completed'}')
            print('===============\n')

    def find_task(self: Self, id: int) -> Task:
        from models import storage

        try:
            task = storage.all()[id]

            return task
        except KeyError as e:
            print('KeyError: Please enter valid task id')
            exit(1)
