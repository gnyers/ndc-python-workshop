===============
Classes, continued
===============

================================================================================
Type Checking
================================================================================

.. sectnum::
   :start: 1
   :suffix: .
   :depth: 2

.. contents:: Contents:
   :depth: 2
   :backlinks: entry
   :local:


Classes, continued
================================================================================

Presentation: `Classes, continued <https://codesensei.nl/presentations/classes-2.html>`_


Magic methods
-------------

- Methods whose name is of the form func

- These functions have special meanings and are pre-defined in the language

We already know about ``__str__``, ``__repr__``, ``__init__``

Examples of other magic methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``__add__``: add two objects together

- ``__eq__``:  implementation of ==

- ``__ne__``: implementation of !=

- ``__len__``: implementation of len() method

See also:

- `Tutorial <https://www.python-course.eu/python3_magic_methods.php>`_

An example
~~~~~~~~~~

Two circles are equal if they have the same radius

.. code:: python

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def __eq__(self, other):
            return self.radius == other.radius

.. code:: python

    c1 = Circle(5)
    c2 = Circle(6)
    c3 = Circle(5)
    c1 == c2 # False
    c1 == c3 # True

Encapsulations
--------------

Private?
~~~~~~~~

Python does not have a **private** keyword. You can mark an attribute as
intended for internal use by prefixing the name with an underscore.

.. code:: python

    class Circle:
        def __init__(self, radius):
            self._r = radius

    c = Circle(5) # We can still access this
    print(c._r)
    c._r = 10  # AND change it
    print(c._r)

Convention: "we are all adults"

Name Mangling
~~~~~~~~~~~~~

If you prefix an attribute name with two underscores, you make it even
harder to reach.

.. code:: python

    class Circle:
        def __init__(self, radius):
            self.__r = radius

    # We can not access this normally
    c = Circle(5)
    print(c.__r)

.. code:: text

    AttributeError: 'Circle' object has no attribute '__r'

Name Mangling
~~~~~~~~~~~~~

.. code:: python

    class Circle:
        def __init__(self, radius):
            self.__r = radius

    # But there is a trick
    c = Circle(5)
    print(c.__dict__)
    print(c._Circle__r)

Property
~~~~~~~~

.. code:: python

    class Circle:
        def __init__(self, radius):
            self.r = radius

        @property
        def diameter(self):
            return 2*self.r

Here ``diameter`` behaves like a read-only attribute.

.. code:: python

    c = Circle(5)
    print(c.diameter)  # Computed on-the-fly from self.r
    c.diameter = 10    # Error!

Setter
~~~~~~

We can add a setter method as well:

.. code:: python

    class Circle:
        def __init__(self, radius):
            self.r = radius

        @property
        def diameter(self):
            return 2*self.r

        @diameter.setter
        def diameter(self, value):
            self.r = value//2

.. code:: python

    c = Circle(5)
    c.diameter = 20
    print(c.r) # Prints 10

Exercises: Magic Methods
=======================

For a list of magic methods, see: `this tutorial <https://www.python-course.eu/python3_magic_methods.php>`_

Exercise 1: Rectangles
-----

Create a class ``Rectangle``. This has two properties: a height and a
 width. Both are arguments of ``__init()__``.

Add a method ``area()`` that returns the area of the rectangle, and a
``__str__`` method that makes it possible to print a rectangle object.
This should also print the area.

Exercise 2: Sorting rectangles
-----

We can make objects sortable by implementing the `<` operator. To do
this, implement the `__lt__(self,other)` method. Make rectangles
sorteable by their area.

Test this by creating a list of rectangle objects and sorting it.

Exercise 3: multiplying rectangles
------

Implement the correct magic methods to make it possible to multiply a
rectangle by an integer `n`. The result should be a rectangle that has
`n` times the height and width:

.. code:: python
   r = Rectangle(2,3)
   x = r*3

`x` should now be a 6x9 rectangle.

Exercise 4:
------

Consider the BankAccount class from before. Add magic methods so that:

- we can compare two bankaccounts using `<`, `>`, and `==`. For these
  operations you only compare balances.

- we can deposit and withdraw money using the `+` and `-` operators
  for a bankaccount and an integer.

The `+` operator should be special: if you add an int to a
bankaccount, you add that amount to the balance.

But if you add two BankAccount objects, you return a new BankAccount
object with the names of the owners added together and the balances
summed as well. The original accounts should be emptied.
