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

Presentation: `Classes (recap) <https://codesensei.nl/presentations/classes.html>`_


Classes
-------

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

Some Extra Examples
===================

.. code:: python

   class Pet:
       "A class representing pet animals"
       def __init__(self, name, species):
           self.name = name       # store the value for name on the name attribute
           self.species = species

   # Creating objects (this calls __init__)
   c = Pet("Tom", "Cat")
   d = Pet("Lassie", "Dog")

   # accessing attributes
   print(c.species)
   print(d.name)


.. code:: python

   class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        self.km = 0

    def drive(self, distance):
        self.km += distance

    def __str__(self):
        return self.model + " " + self.brand + ", kms: " + str(self.km)

.. code:: python

   class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Can't deposit a negative amount!")


    account = BankAccount("RJ", 1000)


Exercises: Warming up
=======================

Exercise 1: BankAccount
-----

Consider the BankAccount example above:

- add a ``__str__()`` method to make it possible to print BankAccount objects.

- add a ``withdraw()`` method to withdraw money from the
  BankAccount. Make sure we cannot withdraw more money than is
  actually in the account. Of course you can also not withdraw a
  negative amount of money.

Exercise 2: Cars
-----

See the Car example above. Create a list of Car instances. Print this
list. What goes wrong?

Add a ``__repr()__`` method to fix this.

Exercise 3: Pizza
-----

Consider the following code:

.. code:: python

    class Topping:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __str__(self):
            return self.name


Start by creating a number of Topping objects, let's say Mozzarella
for $0.20, Tomato Sauce for $0.10, Prosciutto for $0.50.

Then, create a Pizza class. Here are the requirements:

- A pizza is created with a name and a list of toppings (Margherita
  has Mozzarella and Tomato Sauce)

- There should be a method ``Pizza.price()`` that returns the price for
  a pizza. The calculation for this is $2 + the sum of all topping
  prices.

- Make it possible to call ``print()`` on a Pizza object.

Create several Pizza objects to test your code.

Solutions
=========
There are `solutions <solutions_classes_1.rst>`_. for all exercises.
