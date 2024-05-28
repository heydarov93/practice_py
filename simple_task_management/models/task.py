from typing import Self, Union

class Task:
    id: int = 0

    def __init__(self: Self, title, description):
        Task.id: int = Task.id + 1
        self.id: int = Task.id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False

    def __str__(self: Self) -> str:
        pass

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
    
    def to_dict(self: Self) -> dict[str, Union[int, str]]:
        pass