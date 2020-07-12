#kumar
class Shape:

    def name(self, shape):
        print("Shape: %s" % shape,)

class Circle(Shape,):

    def name(self, shape):
        print("class shape %s" % shape)
        self.draw()

    def draw(self):
        print("Printing circle,")
        self.print_sides()

    def print_sides(self):
        print("it has 0 sides,")
        return self
x = int(input("Enter 2:Circle: "))
if x == 2:
 Shape = Circle()
 Shape.name("Circle")
