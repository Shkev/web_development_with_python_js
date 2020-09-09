# creating a class to represent a coordinate point
class Point():
    # always give self as a parameter
    # the __init__ function is like the constructor of the class
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

# creating a Point object
p = Point(2, 8)
print(p.x)
print(p.y)
    
