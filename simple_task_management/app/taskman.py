#!/usr/bin/env python
from models.task import Task
from models.task_manager import TaskManager

import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
      prog='taskman',
      description='Task management system',
      epilog="Thank's for using %(prog)s!")

    subparser = parser.add_subparsers(dest='commands', help='Commands to manipulate tasks')

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
    app = TaskManager()

    args = vars(parse_arguments())

    print(args)

    # operations = {
    #     'add': app.add_task,
    #     'remove': app.remove_task,
    #     'mark': app.mark_task_completed,
    #     'list': app.list_tasks,
    #     'find': app.find_task,
    # }

    # action = operations[args.commands]
    # action()

if __name__ == '__main__':
    main()