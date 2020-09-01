    :Author: Reindert-Jan

.. contents::

Exercises: Magic Methods
=======================

For a list of magic methods, see: `this tutorial <https://www.python-course.eu/python3_magic_methods.php>`_

Exercise 1: Rectangles
-----

.. code:: python

   class Rectangle:

       def __init__(self, height, width):
           self.height = height
           self.width = width

       def area(self):
           return self.width * self.height

       def __str__(self):
           return f"{self.width}x{self.height} = {self.area()}"

Exercise 2: Sorting rectangles
-----

We can make objects sortable by implementing the `<` operator. To do
this, implement the `__lt__(self,other)` method. Make rectangles
sorteable by their area.

Test this by creating a list of rectangle objects and sorting it. Also
implement `__repl__`.

.. code:: python

   class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return f"{self.width}x{self.height} = {self.area()}"

    def __repr__(self):
        return f"{self.width}x{self.height} = {self.area()}"


    print(sorted([Rectangle(10,10), Rectangle(1,1), Rectangle(4,2), Rectangle(2,10)]))


Exercise 3: multiplying rectangles
------

.. code:: python

   class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def __mul__(self, other):
        return Rectangle(self.width*other, self.height*other)

    def __str__(self):
        return f"{self.width}x{self.height} = {self.area()}"

    print(Rectangle(1,1)*5)
