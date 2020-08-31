================================================================================
Solutions: Closures and Decorators
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


Exercise 2: Swapping arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~

Write a function `swap_args` that takes another function as its
arguments but swaps the arguments. You only have to support 2
arguments.

.. code:: python

   def swap_args(func):
       def call_with_swapped_args(a,b):
           return func(b,a)

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

   def cached(func):
       cache = {}
       def call_with_cache(x):
           if x in cache:
               print("I remember this!")
               return cache[x]
           else:
               val = func(x)
               cache[x] = val
               return val
       return call_with_cache

   def some_expensive_calculation(x):
       return x**208 %316 -867

   faster_calc = cached(some_expensive_calculation)
   print(faster_calc(283))  # First time, do the calculation
   print(faster_calc(283))  # Second time: get it from the cache


Exercises: Decorators
---------------------

Exercise 1: HTML
~~~~~~~~~~~~~~~~

Write two decorators `bold` and `italic` that take a string-generating
function and add html tags. You should be able to use them like this:

.. code:: python

   def bold(origfunc):
       def bold_wrapper(*args, **kwargs):
           return '<b>{}</b>'.format( origfunc(*args, **kwargs) )
       return bold_wrapper

   def italic(origfunc):
       def italic_wrapper(*args, **kwargs):
           return '<i>{}</i>'.format( origfunc(*args, **kwargs) )
       return italic_wrapper

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

   secret="p@ssw0rd"

   def auth(origfunc):
       '''Decorate any function to require authentication, i.e.: 'secret'
       '''
       def auth_wrapper(*args, **kwargs):
           if input('Enter secret: ') == 'secret':
               return origfunc(*args, **kwargs)
           else:
               print('Nooo...!')
               return None
       return auth_wrapper

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
       def wrapper(*args, **kwargs):
           return func(json.load(open(data_file)), *args, **kwargs)
       return wrapper

   @from_json
   def get_number_of_legs(legs_data, animal):
       return legs_data[animal]

   print(get_number_of_legs("Bird"))


Exercise 4: Wrapper (Bonus)
~~~~~~~~~~~~~~~~~~~

Consider the following:

.. code:: python

   from functools import wraps

   def wrap(func):
    '''Fill the first argument of func from data_file'''
   @wraps(func)
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
