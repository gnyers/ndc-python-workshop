================================================================================
Closures and Decorators
================================================================================

.. sectnum::
   :start: 1
   :suffix: .
   :depth: 2

.. contents:: Contents:
   :depth: 2
   :backlinks: entry
   :local:


Closures
================================================================================

Presentation: `Closures <https://codesensei.nl/presentations/ndc-closures.html>`_


Introduction
------------

Using functions to create other functions.

Consider
~~~~~~~~

- python functions are *first class citizens*

- functions are objects

- can have properties

- can be passed as function argument

- can be used as a return value

- can be assigned to a variable

Example
~~~~~~~

.. code:: python

    def add(x, y):
        def do_add():
            print('Adding', x, y)
            return x + y
        return do_add

.. code:: text

    >>> a = add(3,4)
    >>> a
    <function do_add at 0x6a670>
    >>> a()
    Adding 3 4
    7

Local Variables
~~~~~~~~~~~~~~~

The inner function refers to variables defined by the outer function.

.. code:: python

    def add(x, y):
        def do_add():
            # `x` and `y` are defined above `add(x, y)`
            print('Adding', x, y)
            return x + y
        return do_add

This still works after ``add()`` has finished

.. code:: text

    >>> a = add(3,4)
    >>> a
    <function do_add at 0x6a670>
    >>> a()
    Adding 3 4      # Where are these values coming from?
    7

Closures
--------

A closure retains the values of all variables needed for the function
to run properly later on.

Example
~~~~~~~

When an inner function is returned as a result, that inner function is
known as a closure.

.. code:: python

    def add(x, y):
        # `do_add` is a closure
        def do_add():
            print('Adding', x, y)
            return x + y
        return do_add

- Think of a closure as a function plus an extra environment that
  holds the values of variables that it depends on

Common uses
~~~~~~~~~~~

- Callback functions

- Delayed evaluation

- Decorators

Delayed Evaluation
~~~~~~~~~~~~~~~~~~

.. code:: python

    def after(seconds, func):
        time.sleep(seconds)
        func()

Usage:

.. code:: python

    def greeting():
        print('Hello Guido')

    after(30, greeting)

Two closures
~~~~~~~~~~~~

.. code:: python

    def add(x, y):
        def do_add():
            print(f'Adding {x} + {y} -> {x+y}')
        return do_add

    def after(seconds, func):
        time.sleep(seconds)
        func()

    after(30, add(2, 3))
    # `do_add` has the references x -> 2 and y -> 3

Note
----

This text was based on from David Beazleys excellent
course
`Practical
Python <https://dabeaz-course.github.io/practical-python/Notes/07_Advanced_Topics/03_Returning_functions.html>`_.

Exercises: Closures
---------------------

Exercise 1: Warming up
~~~~~~~~~~~~~~~~~~~~~~~~~~

Please complete the following program:

.. code:: python

    def never_negative(func):
        """Make sure `func` never returns a negative number"""
        def call_with_modulo(*args, **kwargs):
            return abs(func(*args, **kwargs))
        return  call_with_modulo

    import math
    pow = never_negative(math.pow)

    print(pow(-12,2))




Decorators
==========

Presentation: `Decorators <https://codesensei.nl/presentations/ndc-decorators.html>`_



Introduction
------------

Consider
~~~~~~~~

.. code:: python

    def add(x, y):
        return x + y

Let's say we want to log calls to this function

Logging
~~~~~~~

.. code:: python

    def add(x, y):
        print('Calling add')
        return x + y

    # and another function
    def sub(x, y):
        print('Calling sub')
        return x - y

    # etc..

Problem
~~~~~~~

This is repetitive.

Maybe we can write a function that *adds logging* to existing functions?

Wrappers
--------

Functions

- that take other functions as argument

- change them somehow (e.g. add behaviour)

- return a new function that *wraps* the original one

Example
~~~~~~~

.. code:: python

    def logged(func):
        def wrapper(*args, **kwargs):
            print('Calling', func.__name__)
            return func(*args, **kwargs)
        return wrapper

Usage:

.. code:: python

    def add(x, y):
        return x + y

    logged_add = logged(add)

Decorators
----------

Putting wrappers around functions is extremely common in Python. So
common, there is a special syntax for it.

Example
~~~~~~~

.. code:: python

    def add(x, y):
        return x + y
    add = logged(add)

    # Special syntax
    @logged
    def add(x, y):
        return x + y

These do exactly the same thing.

Note
----

This text was based on David Beazleys excellent
course
`Practical
Python <https://dabeaz-course.github.io/practical-python/Notes/07_Advanced_Topics/03_Returning_functions.html>`_.
-
