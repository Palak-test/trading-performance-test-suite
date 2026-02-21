.. custom-load-shape.rst

Custom Load Shape
=================

Loopa supports custom load shapes to simulate different traffic patterns.

Example:

    class CustomShape:
        def tick(self):
            # Return user count and spawn rate
            return (10, 2)

Custom shapes can be used to model real-world scenarios.
