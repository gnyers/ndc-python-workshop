================================================================================
Segment 1: Functions: Introduction
================================================================================

.. sectnum::
   :start: 1
   :suffix: .
   :depth: 2

.. contents:: Contents:
   :depth: 2
   :backlinks: entry
   :local:



Exercises
================================================================================

Ex01: Find the problem in this function
---------------------------------------

.. code:: python
   :class: pycon

   r = 3
   pi = 3.14

   def circlearea(r=1):
       circlearea = nr ** 2 * pi

   print("The new circle's area is:", circlearea(4))

Ex02: (✪) Define the function ``factorial()``
---------------------------------------------


With the following specifications:

- it takes a single argument ``n``, which is a positive integer number
- returns the factorial value of ``n``, i.e.: the formula: n * n-1 * ... * 2 * 1

  **Sample input**: ``factorial(6)``

  **Expected output**: ``720``

**Bonus**: make sure that the function it returns ``None`` if called with an
invalid value of ``n``

- **Sample input**: ``factorial(-30)``, ``factorial('hello')``
- **Expected output**: ``None``

Ex03: (✪) Classify month into season
------------------------------------

Write the function ``season()``, which:

- will take a single ``str`` value as argument
- the values of the input are limited to the abbreviation of the months in
  English: ``'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
  'Oct', 'Nov', 'Dec'``
- ``season()`` should return the season of the given month

**Sample input**: ``season('Aug')``

**Expected output**: ``summer``


Ex04: (✪✪) Convert between miles and kilometers
-----------------------------------------------

Create a function to convert between miles and kilometers:

- the function should take multiple positional arguments, where each
  argument is a ``str``, e.g.: ``12 km`` or ``1.4 mile`` (the distance unit
  is always separated by at least 1 ``space``)
- let's assume that 1 mile = 1.6 km

**Sample input**: ``convert('10 mile', '12 km', '1.4 mile')``

**Expected output**: ``('16 km', '7.5 mile', '2.2 km')``

Ex05: (✪✪) Define the function ``sorter()``
-------------------------------------------

Which is able to:

- sort a ``list`` of ``str``
- the ``str`` elements are assumed to be numerical values:

  vals = ['23.14', '33.3', '2.8', '13.1', '13.9', '3.4', '23.0', '32.9']

**Expected output**: ``['2.8', '3.4', '13.1', '13.9', '23.0', '23.14', '32.9',
'33.3']``

**Hint**: the ``sorted()`` function will accept a custom sorting function
using the ``key=`` argument.

Ex06: (✪✪) Create the ``avg()`` function
----------------------------------------

Which:

- accept multiple values provided as positional arguments
- will return the average value of the valid numerical values
- disregard any invalid value, i.e. which can not be converted to
  a ``float``

**Sample inputs and their expected outputs**:

- ``avg(33, 22,44,1.2)`` -> ``25.05``
- ``avg(33, 22,44,"1.2")`` -> ``25.05``
- ``avg(33, 22,44,"1.2", 'hello')`` -> ``25.05``

Ex07: (✪✪) De-duplicate
-----------------------

Create the function ``dedup()``, which will:

- de-duplicate the elements of a ``list`` of ``str``'s
- to simplify the detection of duplicates covert the values to
  lower-case
- return a sorted tuple containing the unique ``str``'s

**Sample inputs and their expected outputs**:

- ``dedup('a', 'D', 'a', 'A', 'c')`` -> ``('a', 'c', 'd')``
- ``dedup('Mon', 'tUE', 'mon', 'Tue', 'Wed')`` -> ('mon', 'tue', 'wed')

**Hint**: both the ``dict`` and ``set`` data types have a feature that may
come in handy here


Ex08: (✪✪) Create the function ``counter()``
---------------------------------------------

Specifications:

- takes an arbitrary long ``list`` or ``tuple`` of ``str``'s
- it will count the number of occurrence of each distinct value, and

**Sample input**: ::

 t = '''Beautiful is better than ugly.
 Explicit is better than implicit.
 Simple is better than complex.
 Complex is better than complicated.
 '''

**Expected output**: ::

 {'is': 4, 'better': 4, 'than': 4, 'Beautiful': 1, 'ugly.': 1, 'Explicit': 1,
  'implicit.': 1, 'Simple': 1, 'complex.': 1, 'Complex': 1, 'complicated.': 1}

**Hint**: use a ``dict`` or the appropriate type from the ``collections``
module.

Ex09: (✪✪✪) Analyze text
------------------------

Copy any multi-line text of at least 100 words on your clipboard,
(e.g. the 'Zen of Python' (*) or a part of Python's Wikipedia page)
Paste the text from your clipboard into the variable ``text``

Create the ``analyze()`` function, which will:

- identify each unique word in the text,
- disregard any punctuation characters, e.g.:  ``.,;-()"'``
- for each unique word create a list
- the list should contain all the line number of its occurrences

**Sample input**: ::

 t = '''Beautiful is better than ugly.
 Explicit is better than implicit.
 Simple is better than complex.
 Complex is better than complicated.
 Flat is better than nested.
 Sparse is better than dense.
 Readability counts.
 '''

**Expected output**: ::

 {'beautiful': [1], 'is': [1, 2, 3, 4, 5, 6], 'better': [1, 2, 3, 4, 5, 6],
 'than': [1, 2, 3, 4, 5, 6], 'ugly': [1], 'explicit': [2], 'implicit': [2],
 'simple': [3], 'complex': [3, 4], 'complicated': [4], 'flat': [5], 'nested':
 [5], 'sparse': [6], 'dense': [6], 'readability': [7], 'counts': [7],
 'special': [8, 8], 'cases': [8], "aren't": [8], 'enough': [8], 'to': [8],
 'break': [8], 'the': [8], 'rules': [8], 'although': [9], 'practicality': [9],
 'beats': [9], 'purity': [9], 'errors': [10], 'should': [10], 'never': [10],
 'pass': [10], 'silently': [10], 'unless': [11], 'explicitly': [11],
 'silenced': [11]}

(*) try: ``import this``



Solutions
================================================================================

See also the solutions: `01_func-introduction-exercises-solutions.py <01_func-introduction-exercises-solutions.py>`_


.. vim: filetype=rst textwidth=78 foldmethod=syntax foldcolumn=3 wrap
.. vim: linebreak ruler spell spelllang=en showbreak=… shiftwidth=3 tabstop=3
