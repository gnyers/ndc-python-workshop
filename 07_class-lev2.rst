===============
Classes
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


Classes: Recap
================================================================================

Presentation: `Type Checking <https://codesensei.nl/presentations/classes-2.html>`_


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



.. vim: filetype=rst textwidth=78 foldmethod=syntax foldcolumn=3 wrap
.. vim: linebreak ruler spell spelllang=en showbreak=… shiftwidth=3 tabstop=3
