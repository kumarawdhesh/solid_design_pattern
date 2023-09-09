"""
This principle states that objects of a derived class 
should be able to replace objects of the base class without affecting 
the correctness of the program. In Python, you should ensure that derived 
classes adhere to the contracts defined by their base classes.

Example in Python:

Both Sparrow and Ostrich are derived from the Bird class, and 
they can be used interchangeably in the make_bird_fly function without affecting the correctness of the program.

    """
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly")

def make_bird_fly(bird):
    bird.fly()
