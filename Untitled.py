#!/usr/bin/env python
# coding: utf-8

# In[39]:


class Shape:

    def name(self, shape):
        print("Shape: %s" % shape)


class Rectangle(Shape):

    def name(self, shape):
        print("Child class shape %s" % shape)
        self.draw()

    def draw(self):
        print("Printing rectangle,")
        self.print_sides()

    def print_sides(self):
        print("it has 4 sides")
        return self


class Circle(Shape):

    def name(self, shape):
        print("Child class shape %s" % shape)
        self.draw()

    def draw(self):
        print("Printing circle ,")
        self.print_sides()

    def print_sides(self):
        print("it has 0 sides")
        return self


class Square(Shape):
    def name(self, shape):
        print("Child class shape %s" % shape)
        self.draw()

    def draw(self):
        print("Printing square ,")
        self.print_sides()

    def print_sides(self):
        print("it has 4 sides")
        return self


x = (int)(input("Enter 1:Rectangle 2:Square 3: Circle"))
if x == 1:
    Shape = Rectangle()
    Shape.name("Rectangle")
elif x == 2:
    Shape = Square()
    Shape.name("Square")
elif x == 3:
    Shape = Circle()
    Shape.name("Circle")


# In[ ]:




