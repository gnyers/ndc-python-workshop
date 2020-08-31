================================================================================
Closures and Decorators
================================================================================

.. sectnum::
   :start: 1
   :prefix: Section 
   :suffix: .
   :depth: 2

.. contents:: Contents:
   :depth: 2
   :backlinks: entry
   :local:



Closures
================================================================================

Presentation: `Closures <https://codesensei.nl/presentations/ndc-closures.html>`_

HET PLAN
* Plan
- mostly the text from beazly als presentatie
- extra tekst van jeroen in pres?
- maar ook naar rst -> op github
- voorbeelden van gabor en jeroen als exercises
- typing...?





==========
Decorators
==========

    :Author: Reindert-Jan

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

This presentation was partly copied from David Beazleys excellent
course
`Practical
Python <https://dabeaz-course.github.io/practical-python/Notes/07_Advanced_Topics/03_Returning_functions.html>`_.
-
