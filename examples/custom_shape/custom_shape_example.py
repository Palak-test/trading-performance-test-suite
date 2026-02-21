# custom_shape_example.py

"""
Example of a custom load shape for loopa.
"""

class CustomShape:
    def tick(self):
        return (20, 5)

if __name__ == "__main__":
    shape = CustomShape()
    print(shape.tick())
