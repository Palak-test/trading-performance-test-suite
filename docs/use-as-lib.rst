.. use-as-lib.rst

Using Loopa as a Library
========================

Loopa can be imported and used as a Python library in your own projects.

Example:

    import loopa
    dispatcher = loopa.Dispatcher()
    dispatcher.add_task(my_task)
    dispatcher.run()

See API documentation for details.
