class Task:
    id: int = 0

    def __init__(self, title, description):
        Task.id: int = Task.id + 1
        self.id: int = Task.id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False

    def mark_as_completed(self):
        self.completed = True
    
    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, value: str):
        if (value == ''):
            raise ValueError('Please enter at least 1 (one) character for title')

        if (type(value) is not str):
            raise TypeError('Title must be a string')

        self._title: str = value
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, value: str):
        if (type(value) is not str):
            raise TypeError('Description must be a string')

        self._description: str = value
