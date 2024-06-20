from app.models.task import Task
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
        from app import storage

        new_task: Task = Task(title, description)
        storage.new(new_task)
        # for file storage
        # storage.save()
        # return new_task.id
    
    def remove_task(self: Self, id: int) -> None:
        from app import storage

        return storage.delete(id)

        # for file storage
        # storage.save()
    
    def mark_task_completed(self: Self, id: int) -> None:
        from app import storage

        # for file storage
        # tasks: dict[str, Task] = storage.all()
        # tasks[id].mark_as_completed()
        storage.mark(id)
        # storage.save()
    
    def list_tasks(self: Self) -> None:
        from app import storage

        for task in storage.all():
            print(f'id: {task[0]}')
            print(f'title: {task[1]}')
            print(f'description: {task[2]}')
            print(f'status: {'Completed' if task[3] else 'Not completed'}')
            print('===============\n')

    def find_task(self: Self, id: int) -> Task:
        from app import storage

        try:
            task = storage.find(id)

            return task
        except KeyError:
            print('KeyError: Please enter valid task id')
            exit(1)
