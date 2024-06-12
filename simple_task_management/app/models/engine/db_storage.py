import psycopg2
from typing import Self

from config import Config
from models.task import Task

class DBStorage:
    """ Database management class for tasks """
    def __init__(self: Self):
        """ Connect to the PostgreSQL database server """
        config = Config()
        configs = config.configs

        try:             
            self.conn = psycopg2.connect(**configs)
            self.cur = self.connection.cursor()
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
    
    def new(self: Self, task_object: Task):
        """ Inserts new task into tasks table"""
        try:
            title, description = task_object.to_dict()
            sql = """INSERT INTO tasks(title, description)
                     VALUES(%s) RETURNING id;"""

            self.cur.execute(sql, (title, description))
            rows = self.cur.fetchone()
            print(rows)
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
        finally:
            self.conn.commit()
    
    def mark(self: Self, id: int):
        """ Marks task as completed """
        try:
            
            sql = """UPDATE tasks
                        SET completed = %s
                        WHERE id = %s;"""

            self.cur.execute(sql, (True, id))
            row = self.cur.fetchone()
            print(row)
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
    
    def all(self: Self):
        """ Returns all tasks from database """
        try:
            
            sql = """SELECT * FROM tasks;"""

            self.cur.execute(sql)
            rows = self.cur.fetchall()
            print(rows)
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def save(self: Self):
        if self.connect:
            self.connect.commit()

    def close(self: Self):
        """ Closes the connection and the cursor """
        self.conn.close()
        self.cur.close()
