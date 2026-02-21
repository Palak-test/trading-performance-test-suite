.. tasksets.rst

Tasksets
========

Tasksets define user behavior in loopa. Each taskset is a collection of tasks that simulate actions performed by users.

Example:

    def user_task():
        print("User is browsing homepage")

    def another_task():
        print("User is searching")

Tasksets can be added to the dispatcher for execution.
