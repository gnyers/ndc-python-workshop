    :Author: Reindert-Jan

.. contents::

1 Solutions: classes
--------------------

1.1 BankAccount
~~~~~~~~~~~~~~~

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
                if amount <= self.balance:
                    self.balance -= amount
                    return self.balance
                else:
                    print("Insufficient balance!")
            else:
                print("Can't withdraw nonpositive amount!")

        def __str__(self):
            return "Bankaccount for " + self.name + ", balance: " + str(self.balance)

1.2 Pizza
~~~~~~~~~

.. code:: python

    class Topping:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __str__(self):
            return self.name

        def __repr__(self):
            return self.name


    class Pizza:
        base_price = 5
        def __init__(self, name, toppings):
            self.name = name
            self.toppings = toppings

        def price(self):
            topping_price = 0
            for t in self.toppings:
                topping_price += t.price
            return Pizza.base_price  + topping_price

        def __str__(self):
            return "Pizza " + self.name + " with: " + str(self.toppings)


    # Example use of pizza class
    if __name__ == "__main__":
        p = Pizza("Margherita", [Topping("Cheese", 1), Topping("Tomato", 0.5)])
        print(p)
        print(p.price())
