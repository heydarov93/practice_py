#!/usr/bin/env python
from models.task import Task
from models.task_manager import TaskManager
import argparse


parser = argparse.ArgumentParser(description='Task management system')
parser.add_argument('add', help='Creates new task')

args = parser.parse_args()
print(args.add)
