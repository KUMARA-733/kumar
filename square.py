#kumar
class Shape:

    def name(self, shape):
        print("Shape: %s" % shape)

class Square(Shape):
    def name(self, shape):
     print("class shape %s" % shape,)
     self.draw()

    def draw(self):
     print("Printing square ,")
     self.print_sides()

    def print_sides(self):
        print("it has 4 sides,")
        return self
x = int(input("Enter 3: Square"))
if x == 3:
 Shape = Square()
 Shape.name("Square")
