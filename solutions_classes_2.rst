===============
Solutions: Classes, pt 2
===============

.. sectnum::
   :start: 1
   :suffix: .
   :depth: 2

.. contents:: Contents:
   :depth: 2
   :backlinks: entry
   :local:
    :Author: Reindert-Jan

.. contents::

Solutions: Magic Methods
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


Exercise 4: BankAccount
----------------------

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

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return self.balance
            else:
                print("Not enough money :(")
        else:
            print("Can't withdraw a negative amount!")

    # Note: we only need one comparison operator for < and >
    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        if isinstance(other, int):
            self.deposit(other)
            return self
        else:
            nw_acct = BankAccount(f"{self.name} & {other.name}", self.balance + other.balance)
            self.balance = 0
            other.balance = 0
            return nw_acct

    def __sub__(self, other):
        self.withdraw(other)
        return self


    def __str__(self):
        return f"account: {self.name}: {self.balance}"

    account1 = BankAccount("RJ", 1000)
    account2 = BankAccount("Scrooge McDuck", 10000000)
    print(account1 < account2)
    print(account1 > account2)
    print(account1 == account2)

    account3 = BankAccount("Irina", 1000)
    together = account1 + account3
    print(together)
    together += 200
    print(together)
    print(together - 2200)


Solutions: Properties
=====================

Exercise 1: fullname
---------------------

.. code:: python

   class Person:
       def __init__(self, firstname, lastname):
           self.firstname = firstname
           self.lastname = lastname

       @property
       def fullname(self):
           return f"{self.firstname} {self.lastname}"


Exercise 2: square
---------------------

On your rectangle class, add a boolean property `is_square` that is
true when width and height are the same.

Usage:

.. code:: python

   class Rectangle:
       ...

       @property
       def is_square(self):
           return self.height == self.width

Exercise 3: password
-------------------

.. code:: python

   class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.__password = None

    ...

    @property
    def password(self):
        return ""

    @password.setter
    def password(self, new_pwd):
        self.__password = new_pwd[::-1] # very sophisticated encryption scheme

    def check_password(self, password):
        if self.__password is None:
            return False # No password set
        else:
            return password[::-1] == self.__password

   account1 = BankAccount("RJ", 1000)
   account1.password = "secret"
   print(account1._BankAccount__password) # we are actually storing an "encrypted" password
   print(account1.check_password("hi!"))
   print(account1.check_password("secret"))
