# dispatch_test.py

"""
Example script for testing dispatcher in loopa.
"""

from loopa.dispatch import Dispatcher

def task1():
    print("Task 1 executed")

def task2():
    print("Task 2 executed")

if __name__ == "__main__":
    dispatcher = Dispatcher()
    dispatcher.add_task(task1)
    dispatcher.add_task(task2)
    dispatcher.run()
