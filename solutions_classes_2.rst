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
