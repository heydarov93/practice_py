from typing import Self, Union

class Task:
    id: int = 0

    def __init__(self: Self, title: str, description: str, id: int=None):
        if id is None:
            Task.id: int = Task.id + 1
            self.id: int = Task.id
            self.completed: bool = False
        else:
            self.id: int = id
        
        self.title: str = title
        self.description: str = description

    def __str__(self: Self) -> str:
        id = f'id: {self.id}\n'
        title = f'title: {self.title}\n'
        description = f'description: {self.description}\n'
        status = f'status: {'completed' if self.completed else 'not completed'}'
        return id + title + description + status

    def mark_as_completed(self):
        self.completed = True
    
    @property
    def title(self: Self) -> str:
        return self._title

    @title.setter
    def title(self: Self, value: str):
        if (value == ''):
            raise ValueError('Please enter at least 1 (one) character for title')

        if (type(value) is not str):
            raise TypeError('Title must be a string')

        self._title: str = value
    
    @property
    def description(self: Self) -> str:
        return self._description
    
    @description.setter
    def description(self: Self, value: str):
        if (type(value) is not str):
            raise TypeError('Description must be a string')

        self._description: str = value

    def to_dict(self: Self):
        """Returns dictionary representation of a Task obj"""
        return self.__dict__
