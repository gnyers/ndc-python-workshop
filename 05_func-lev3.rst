======================
Functional Programming
======================

.. sectnum::
   :start: 1
   :suffix: .
   :depth: 2

.. contents:: Contents:
   :depth: 2
   :backlinks: entry
   :local:


Functional Programming
================================================================================

Presentation: `Functional Programming <https://codesensei.nl/presentations/functional.html>`_

What is functional programming?
-------------------------------

::

    Functional programming is a programming paradigm where programs are
    constructed by applying and composing functions.


In Python
~~~~~~~~~

We mostly mean transforming sequences of data through application of functions, using

- comprehensions

- generators

- lambda, map, filter

- Note that comprehensions are preferred over lambda/map/filter

List Comprehensions
-------------------

A list comprehension is a concise way to generate a list. The syntax
looks like this:

.. code:: python

    [ operation for var in input_data [if test] ]

 ``input_data`` has to be iterable. Each element will be
assigned to ``var`` in turn.

Optional test; only those elements that pass the test
will be sent to the output.

Example
-------

.. code:: python

    l = [ x*x for x in range(100) ] # first 100 squares
    vowels = [ c for c in "hi everyone!" if c in "aeiouu" ] # "ieeyoe"
    coords = [(x,y) for x in range(4) for y in range(4)] # nested

List comprehensions can filter and transform your data in a single
line.

Other comprehension
~~~~~~~~~~~~~~~~~~~

A list comprehension creates a list. We also have
Dict and set comprehensions:

.. code:: python

    products = ["bread", "cheese", "milk"]
    prices = [2,5,1]
    p = {products[i].capitalize(): float(prices[i]) for i in range(3)}
    n = {name for name in products if len(name) > 4}

Generator expressions
---------------------

Like list comprehensions, but return a generator object instead of a list.

This allows for lazy computation.

.. code:: python

    numbers = (x**x for x in range(1000,1000000))

This returns immediately.

.. code:: text

    <generator object <genexpr> at 0x10abebd60>

Evaluation
~~~~~~~~~~

The generator object promises to calculate its elements on demand. We
can ask for the next element:

.. code:: python

    next(numbers) # 1000**1000
    next(numbers) # 1001**1001
    next(numbers) # 1002**1002

Or convert the whole thing to a list at once:

.. code:: python

    list(numbers) # will take a long time

Evaluation 2
~~~~~~~~~~~~

You can use the generator in a for loop

.. code:: python

    for n in numbers:
        # Calculate next number
        print(f"{n} is a large number!")

or in another comprehension:

.. code:: python

    strings = (f"{n} is a large number!" for n in numbers)

This last example still does no computations at all!

Itertools
~~~~~~~~~

The `itertools <https://docs.python.org/3.8/library/itertools.html>`_
package has some nice functions to work with generators.

.. code:: python

    from itertools import islice
    # Take first five elements
    first_five = islice(numbers,0,5)

This again, returns a generator.

Note that you cannot do (why?):

.. code:: python

    numbers[0,5] # Error

Old-style functional programming
--------------------------------

The traditional way of functional programming uses 3 main functions:
``map()``, ``filter(), reduce()``, often in combination with ``lambda()``.

All of these functions return generators.

We will not go into reduce.

Map
~~~

Apply a function to a sequence and return a sequence of the results.

.. code:: python

    prices = ["$0.50", "$0.30", "€100", "$210.20", "220€"]
    to_f = list(map(lambda s: float(s[1:]), prices))

You can write this as a comprehension:

.. code:: python

    to_f = [ float(s[1:]) for s in prices ]

Filter
~~~~~~

Apply a function to a sequence and return only those values for which
the function returns a true value.

.. code:: python

    prices = ["$0.50", "$0.30", "€100", "$210.20", "220€"]
    dollars = list(filter(lambda s: s[0] == '$', prices))

As a comprehension:

.. code:: python

    to_f = [ p for p in prices if p[0] == '$' ]

Map and filter
~~~~~~~~~~~~~~

Combining both:

.. code:: python

    prices = ["$0.50", "$0.30", "€100", "$210.20", "220€"]
    to_f = list(map(lambda s: float(s[1:]), filter(lambda s: s[0] == '$', prices)))

Comprehension:

.. code:: python

    to_f = [ float(s[1:]) for s in prices if s[0] == '$']


Exercises: Warming up
=======================

Exercise 1: numbers
-----------------

Write a list comprehension that returns all numbers below 1000 that
are divisable by 13 and 29.


Exercise 2: person data
----------------

Given the following data:

.. code:: python

   students = [("Laurens", 27),
            ["Ruben", 27],("Roel", 29),["Jan", 27],["Max", 26],
            ["Maikel", 29],["Dieter", 24],]

Write list comprehensions that:

- Return a list with each name in upper case
- Return a list of names of everyone older than 26
- Return a list where each element has the name and age swapped

Exerise 3: puzzle
----------------

Given the following:

.. code:: python

   species = [ { 'name': 'Human', 'legs': 2, 'movement': 'walk' },
               { 'name': 'Dog', 'legs': 4, 'movement': 'walk' },
               { 'name': 'Duck', 'legs': 2, 'movement': 'fly' },
               { 'name': 'Whale', 'legs': 0, 'movement': 'swim' },
             ]

   individuals = [{'name': 'Bob', 'species': 'Human'},
                   {'name': 'Daffy', 'species': 'Duck'},
                   {'name': 'Lassie', 'species': 'Dog'},
                   {'name': 'Moby', 'species': 'Whale'},
                   {'name': 'Lisa', 'species': 'Human'},
                   {'name': 'Pluto', 'species': 'Dog'}]


Determine the total number of legs for `individuals` by using comprehensions.
