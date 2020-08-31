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
            # ... insert your code here ...

    return  call_with_modulo

    import math
    pow = never_negative(math.pow)

    print(pow(-12,2))


Exercise 2: Swapping arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~

Write a function `swap_args` that takes another function as its
arguments but swaps the arguments. You only have to support 2
arguments.

.. code:: python

   def swap_args(func):
       # ... your code here ...

   tnirp = swap_args(print)
   tnirp("Good", "morning")  # output: "morning Good"

   from math import pow
   wop = swap_args(pow)
   print(wop(2,5))  # print 25 (5^2) instead of 32 (2^5)

Exercise 3: Caching
~~~~~~~~~~~~~~~~~~~

Write a function `cached` that remembers the results of function
calls. It only supports functions of one argument. Hint: use a dict to
store the results of previous function calls.


.. code:: python

   def some_expensive_calculation(x):
       return x**208 %316 -867

   faster_calc = cached(some_expensive_calculation)
   print(faster_calc(283))  # First time, do the calculation
   print(faster_calc(283))  # Second time: get it from the cache


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

Links
-----

For extra reading I recommend `this blog by Miguel Grinberg <https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-i-function-registration>`_.

Exercises: Decorators
---------------------

Exercise 1: HTML
~~~~~~~~~~~~~~~~

Write two decorators `bold` and `italic` that take a string-generating
function and add html tags. You should be able to use them like this:

.. code:: python

   @italic
   def say_in_bold_and_italic(text):
       return text


   @bold
   def say_in_bold(text):
       return text


   print(say_in_bold("hi"))
   print(say_in_bold_and_italic("bye"))


Exercise 2: Authorization
~~~~~~~~~~~~~~~~~~~~~~~~~

Write a decorator `auth` that makes a function require authorization.
Any function decorated in this way, will ask for a password. If the
password is not entered correctly, you refuse to execute the code.

.. code:: python

   @auth
   def get_private_data():
       return something_very_secret

Exercise 3: JSON
~~~~~~~~~~~~~~~~

Write a decorator from_json that will fill the first argument of the
function it decorates with data read from a json file.

Hint: use the `json.load()` function.

Example: given the following file `legs.json`:

.. code:: json

   {
     "Dog": 4,
     "Cat": 3,
     "Bird": 2,
     "Whale": 0
   }


.. code:: python

   import json

   data_file = "legs.json"

   def from_json(func):
       '''Fill the first argument of func from data_file'''
       # ... your code here ...

   @from_json
   def get_number_of_legs(legs_data, animal):
       return legs_data[animal]

   print(get_number_of_legs("Bird"))

This should print "2" :)

As a bonus exercise: try to add the filename of the json file as an
argument to the decorator. This works slightly different; see `this
article
<https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-iii-decorators-with-arguments>`_


Exercise 4: Wrapper (Bonus)
~~~~~~~~~~~~~~~~~~~

Consider the following:

.. code:: python

   def wrap_func(func):
       '''Fill the first argument of func from data_file'''
       def my_wrapper(*args, **kwargs):
           """This is the function wrapper"""
           return func(*args, **kwargs)
       return my_wrapper


   @wrap_func
   def my_func():
       """This is my function"""
       print("hi!")

   print(my_func)
   print(help(my_func))

Run the program and carefully examine the output. We are printing
information about `my_func` but that is not what we get to see.

This can be confusing, especially when debugging your code. The
solution is something called `functools.wraps`, which is explained
`here
<https://lerner.co.il/2019/05/05/making-your-python-decorators-even-better-with-functool-wraps/>`_.


Solutions
=========
There are `solutions <solutions_closures_decorators.rst>`_. for all exercises.
