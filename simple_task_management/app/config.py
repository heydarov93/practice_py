from configparser import ConfigParser
from typing import Self
import os


class Config:
    """ Database configuration """

    def __init__(self: Self, filename: str = 'database.ini', section: str = 'postgresql'):
        parser = ConfigParser()
        parser.read(filename)

        configs = {}

        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                configs[param[0]] = param[1]
        else:
            raise Exception('Section {} not found in the {} file'.format(section, filename))
        
        self.configs: dict[str, str] = configs

    @property
    def configs(self: Self) -> dict[str, str]:
        """ Getter for private config """

        # return shallow copy of config dictionary
        return self.__configs.copy()
    
    @configs.setter
    def configs(self: Self, value: dict[str, str]) -> None:
        """ Setter for private config """
        self.__configs = value.copy()
