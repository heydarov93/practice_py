from typing import Self, Any
from models.task import Task
import json

class FileStorage:
    __tasks: dict[int, Task] = {}
    __file_path: str = 'tasks.json'

    def all(self: Self) -> dict[int, Task]:
        """Returns list of the all tasks"""

        temp: dict[int, Task] = {}

        for key, value in self.__tasks.items():
            temp[key] = value
        
        return temp

    def new(self: Self, obj: Task) -> None:
        """Adds new task to the dictionary"""
        key: int = obj.id
        self.__tasks[key] = obj
    
    def delete(self: Self, id: int) -> None:
        """Deletes a task"""

        tasks: dict[int, Task] = self.__tasks
        del tasks[id]

    def save(self) -> None:
        """Saves all tasks into the file"""
        with open(self.__file_path, 'w', encoding='utf-8') as afile:
            temp: dict[Any, dict[str, Any]] = {}

            for key, value in self.__tasks.items():
                temp[key] = value.to_dict()


            temp['last_id'] = Task.id
            json.dump(temp, afile)
    
    def reload(self: Self) -> None:
        """Reloads all tasks from file"""
        try:
            with open(self.__file_path, encoding='utf-8') as afile:
                tasks = json.load(afile)
                Task.id = tasks.pop('last_id')

                for key, task_dict in tasks.items():
                    obj = Task(
                        task_dict['_title'],
                        task_dict['_description'],
                        task_dict['id'])

                    obj.completed = task_dict['completed']
                    self.new(obj)
        except FileNotFoundError:
            pass
