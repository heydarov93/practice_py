import psycopg2
from typing import Self, Any

from app.config import Config
from app.models.task import Task

class DBStorage:
    """ Database management class for tasks """

    def __init__(self: Self):
        """ Connect to the PostgreSQL database server """
        config = Config()
        configs = config.configs

        try:             
            self.conn = psycopg2.connect(**configs)
            self.cur = self.conn.cursor()
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
    
    def new(self: Self, task_object: Task):
        """ Inserts new task into tasks table"""
        try:
            task_dict = task_object.to_dict()

            _title = task_dict['_title']
            _description = task_dict['_description']
            completed = task_dict['completed']

            sql = """INSERT INTO tasks(title, description, completed)
                     VALUES(%s, %s, %s) RETURNING id;"""

            self.cur.execute(sql, (_title, _description, bool(completed)))
            rows = self.cur.fetchone()
            self.conn.commit()

            # get id of the last inserted task
            return rows[0]
        except (psycopg2.DatabaseError, Exception) as error:
            print('Error:')
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
            row = self.cur.rowcount
            print(row)
            self.conn.commit()
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
    
    def all(self: Self):
        """ Returns all tasks from database """
        try:
            
            sql = """SELECT * FROM tasks ORDER BY id ASC;"""

            self.cur.execute(sql)
            rows = self.cur.fetchall()
            return rows
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
    
    def find(self: Self, id: int) -> tuple[Any]:
        """ Returns all tasks from database """
        try:
            
            sql = """SELECT * FROM tasks WHERE id = %s;"""

            self.cur.execute(sql, (id, ))
            row = self.cur.fetchone()
            return row
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def delete(self: Self, id: int) -> bool:
        """ Returns all tasks from database """
        try:
            
            sql = """DELETE FROM tasks WHERE id = %s;"""

            self.cur.execute(sql, (id, ))
            rows_deleted = self.cur.rowcount
            self.conn.commit()
            return rows_deleted
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def close(self: Self):
        """ Closes the connection and the cursor """
        self.conn.close()
        self.cur.close()


# storage = DBStorage()
# task = Task('code', 'practice')
# storage.new(task)