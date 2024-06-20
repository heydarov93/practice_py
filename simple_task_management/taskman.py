#!/usr/bin/env python
from app.models.task_manager import TaskManager
from app import storage

import argparse
from typing import Callable, Any


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
      prog='taskman',
      description='Task management system',
      epilog="Thank's for using %(prog)s!")

    subparser = parser.add_subparsers(title='Operations', description='Commands to manipulate tasks', dest='commands', required=True)

    add_task = subparser.add_parser('add', help='Creates new task')
    add_task.add_argument('title', type=str, help='Title for the task')
    add_task.add_argument('description', type=str, help='Task description')

    remove_task = subparser.add_parser('remove', help='Removes task')
    remove_task.add_argument('id', type=int, help='Id of the task to delete')

    mark_task = subparser.add_parser('mark', help='Marks task as completed')
    mark_task.add_argument('id', type=int, help='Id of the task to mark as completed')

    subparser.add_parser('list', help='Prints all tasks')

    find_task = subparser.add_parser('find', help='Finds specific task')
    find_task.add_argument('id', type=int, help='Id of the task to find')

    args = parser.parse_args()
    
    return args


def main() -> None:
    app: TaskManager = TaskManager()

    args: dict = vars(parse_arguments())

    operations:dict = {
        'add': app.add_task,
        'remove': app.remove_task,
        'mark': app.mark_task_completed,
        'list': app.list_tasks,
        'find': app.find_task,
    }

    if args['commands'] == 'add':
        action: Callable[[str, str], int] = operations[args['commands']]
        action(args['title'], args['description'])
        return
    
    if args['commands'] == 'list':
        action: Callable[[None], None] = operations[args['commands']]
        action()
        return
    
    action: Callable[[int], Any] = operations[args['commands']]
    task = action(args['id'])
    
    if task:
        print(task)
    
    storage.close()


if __name__ == '__main__':
    main()
