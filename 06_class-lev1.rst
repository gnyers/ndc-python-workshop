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

Presentation: `Type Checking <https://codesensei.nl/presentations/classes.html>`_


Classes
~~~~~~~

Give structure to your code by grouping

- data (values) and

- code (functions)

Create our own data types called classes.

Objects
~~~~~~~

Everything in a Pyton is an object. An object's class is also its type.

.. code:: python

    print("hi".__class__)
    print((5).__class__)
    print(None.__class__)

Custom classes
~~~~~~~~~~~~~~

Lets create our own datatype to store data for a person

.. code:: python

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            print("Hi! My name is", self.name)

Interpretation
~~~~~~~~~~~~~~

A class is like a "blueprint" for objects. The Person class defines
properties and behaviour shared by all Persons.

.. code:: python

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            print("Hi! My name is", self.name)

Instances
~~~~~~~~~

.. code:: python

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        ...

.. code:: python

    p = Person("RJ", 40)

Instances
~~~~~~~~~

.. code:: python

    p = Person("RJ", 40)

- p is an object of class Person!

- p is created by calling Person like it was a function.

- This effectively calls ``__init__``, which "constructs" the object

- The arguments to ``__init__`` are the information needed to build the object

Attributes
----------

Dot
~~~

Access the attributes of an object by using a dot

.. code:: python

    p = Person("RJ", 40)
    p2 = Person("Jake", 35)
    print(p.name)
    print(p2.age)

    # Attribute has to exist
    print(p.something) # Error

Methods
~~~~~~~

Methods are the function attributes of a class.

.. code:: python

    class Person:
        def __init__(self, name, age):
            ...

        def greet(self):
            print("Hi! My name is", self.name)

        def get_year_of_birth(self):
            return 2020 - self.age

.. code:: python

    p.greet()
    print(p.get_year_of_birth())

Self
~~~~

.. code:: python

    class Person:
        def __init__(self, name, age):
            ...

        def greet(self):
            print("Hi! My name is", self.name)

        def get_year_of_birth(self):
            return 2020 - self.age

- ``self`` is the first argument of each method

- ``self`` points to the object that the method is working on

String representation
---------------------

.. code:: python

    p = Person("RJ", 40)
    str(p)  # or print(p)

Output:

.. code:: text

    <__main__.Person object at 0x1058f93a0>

str
~~~

Used to create a human-readable string from an object.

We can influence its behaviour by writing a method ``__str__``,
which should return a string.

.. code:: python

    class Person:
        ...

        def __str__(self):
            return "Hi, I am " + self.name

.. code:: python

    p = Person("RJ", 40)
    str(p)  # or print(p)

.. code:: text

    "Hi, I am RJ"

repr
~~~~

Used to create a more detailed representation for programmers (or
other programs).

.. code:: python

    class Person:
        ...

        def __repr__(self):
            return f"Person({self.name},{self.age})"

Theoretically, the output of ``__repr__`` should be useable with
``eval()`` to re-create the object
