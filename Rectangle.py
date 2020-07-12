#kumar
class Shape:

    def name(self, shape):
        print("Shape: %s" % shape)

class Rectangle(Shape,):
    def name(self, shape):
        print("class shape %s" % shape,)
        self.draw()

    def draw(self):
        print("Printing rectangle,")
        self.print_sides()

    def print_sides(self):
        print("it has 4 sides,")
        return self
x = int(input("Enter 1:Rectangle:  "))
if x == 1:
    Shape = Rectangle()
    Shape.name("Rectangle")
