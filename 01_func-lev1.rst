================================================================================
Segment 1: Functions: a recap
================================================================================

.. sectnum::
   :start: 1
   :suffix: .
   :depth: 2

.. contents:: Contents:
   :depth: 2
   :backlinks: entry
   :local:


Recap
================================================================================

Functions:

- are callable objects: they represent one or more statements
- the purpose of functions is to be able to re-use these statements all over
  our program(s)
- can take a fixed or variable number of arguments
- return exactly one object, which may be a collection object. This is the way
  to return multiple objects from the function.
- the return object is by default the ``None`` object, unless *overwritten* by
  the expression of the first ``return`` statement (e.g.: ``return a + b``)
- can take a function as argument and return a function (also known as:
  "first-class" functions)


Declaring functions
================================================================================

Using the ``def`` keyword
--------------------------------------------------------------------------------

The primary syntax to define functions.

Example
^^^^^^^

.. code:: python
   :class: python-code

   def add(a, b):
       return a + b

- ``def`` keyword will define a function object
- the first row of the definition (i.e.: the one containing the ``def``
  keyword) contains a number of important attributes of the function and its
  arguments:

  #. the function's name (in this case: ``add``)
  #. how many arguments the function will take (in this case: exactly 2)
  #. for each argument:

     - whether or not it's a mandatory or optional argument, and
     - whether or not this argument may be provided a positional-only,
       keyword-only or both ways

- the function's code block will define if the return value is something else
  than the ``None`` object.

Single-expression functions
--------------------------------------------------------------------------------

The purpose of the ``lambda`` keyword is to define simple functions, which
often are used only once.

Typical example of using lambda functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python
   :class: pycon

   >>> team
   ['evE', 'ALEX', 'joe', 'dAn', 'Oli']

   >>> sorted(team)
   ['ALEX', 'Oli', 'dAn', 'evE', 'joe']

   >>> sorted(team, key=lambda n: n.lower())
   ['ALEX', 'dAn', 'evE', 'joe', 'Oli']

- The elements of list ``team`` are mixed-case strings
- Sorting such a list is not trivial, especially if we must preserve the case
- The ``"sorted()"`` function's ``"key="`` argument is provided with
  a callable object defined as a lambda function: ``lambda n: n.lower()``.
- The ``lambda`` function is usually no longer needed after this sorting.


Fuction Arguments
================================================================================

Argument passing
--------------------------------------------------------------------------------

Argument passing to functions in Python is a bit unusual compared to other
programming languages. In this context, the usual terms ``by-reference`` and
``by-value`` do not apply for Python.

Example
^^^^^^^

.. code:: python
   :number-lines: 1
   :class: python-code

   name = 'Sponge Bob'
   pals = ['Patrick', 'Sandy', 'Gary']

   def mixup(character, friends):
       character = 'Mr. Krabs'
       friends.clear()

   mixup(name, pals)
   print(f'Character name: {name}')
   print(f"Character's fiends: {pals}")

- When executed, this above example will print: ::

   Character name: Sponge Bob
   Character's firends: []

- the main program's ``"name"`` variable is not updated, so this would suggest
  passing ``by-value``

- on the other hand the variable ``"pals"`` is emptied by the function, which
  would suggest passing ``by-reference``

- Python in fact has its own way to pass arguments: pass ``by-assignment``.

  This behavior boils down to the following rule-of-thumb:

  - mutable objects (e.g.: ``list``, ``dict``, ``set``) will behave as if they
    were passed ``by-reference``.

    That is: a function may change the content of the object.

  - immutable objects (e.g.: ``int``, ``str``, ``tuple``) will behave is if
    passed ``by-value``.

    That is: any re-assignment done by the function will have no effect on the original value.


Mandatory arguments
--------------------------------------------------------------------------------

Our earlier example requires exactly two arguments ``a`` and ``b``, no more
and no less.

.. code:: python
   :class: python-code

   def add(a, b):
       return a + b

**Example usage 1**: too few arguments:

.. code:: python
   :class: pycon

   >>> add()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: add() missing 2 required positional arguments: 'a' and 'b'

   >>> add(1)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: add() missing 1 required positional argument: 'b'

**Example usage 2**: too many arguments:

.. code:: python
   :class: pycon

   >>> add(1,2,3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: add() takes 2 positional arguments but 3 were given

**Example usage 3**: exactly right

.. code:: python
   :class: pycon

   >>> add(3, 10)
   13
   >>> add((1,2,3), (4,))
   (1, 2, 3, 4)


Optional arguments
--------------------------------------------------------------------------------

By assigning a default value to an argument, it is no longer required.

.. code:: python
   :class: python-code

   def mul(a, b=1):
       return a * b

**Example usage 1**: if argument ``"b"`` is not provided, its value will be
``1``:

.. code:: python
   :class: pycon

   >>> mul(3)
   3
   >>> mul(3, 2)
   6

**Example usage 2**: be careful: argument ``"a"`` is still required!

.. code:: python
   :class: pycon

   >>> mul(b=3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: mul() missing 1 required positional argument: 'a'


Providing arguments to functions
================================================================================

There are two possible notations for an argument to be passed to a function:

#. as a positional argument:

   .. code:: python
      :class: pycon

      >>> def add(a,b):
      ...     print(f'arg "a": {a}')
      ...     print(f'arg "b": {b}')
      ...     return a + b
      ...
      >>> add(2, 3)
      arg "a": 2
      arg "b": 3
      5

   In this example argument ``"a"`` has been assigned the object ``2``, and
   ``"b"`` got ``3``.

   The reason for this is the positions of resp. ``"a"`` and ``"b"`` on the
   function's argument list, and the order in which ``2`` and ``3`` have been
   provided.

#. as a keyword argument:

   .. code:: python
      :class: pycon

      >>> add(a=2, b=3)
      arg "a": 2
      arg "b": 3
      5

   Here the both arguments have explicitly been assigned.

   .. code:: python
      :class: pycon

      >>> add(b=3, a=2)
      arg "a": 2
      arg "b": 3
      5

   In this case it doesn't even matter in what order they are being provided.


**Best practice**: In general using keyword arguments is preferable, because
"Explicit is better than implicite"


Variable number of arguments
================================================================================

When creating a function, we often wish to be able to consume a variable
number of arguments.

Variable number of postional arguments
--------------------------------------------------------------------------------

**Example**:

.. code:: python
   :number-lines: 1
   :class: python-code

   def greet(*people):
       for person in people:
           print(f'Hello {person}')

The notation ``*people`` will instruct Python to collect every positional
arguments into a ``tuple`` and assign it to the variable ``people``.

.. code:: python
   :class: pycon

   >>> greet('Jenny', 'Joe', 'Adele') 
   Hello Jenny
   Hello Joe
   Hello Adele

**Note**: the function ``greet()`` can only process positional arguments:

.. code:: python
   :class: pycon

   >>> greet('Jenny', 'Joe', p3='Adele')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: greet() got an unexpected keyword argument 'p3'


Variable number of keyword arguments
--------------------------------------------------------------------------------

**Example**:

.. code:: python
   :number-lines: 1
   :class: python-code

   def show(**attributes):
      for attr in attributes:
          print(f'{attr} = {attributes[attr]}')

The notation ``*attributes`` will instruct Python to collect every positional
arguments into a ``tuple`` and assign it to the variable ``people``.

TODO!!!

Variable number of postional and keyword arguments
--------------------------------------------------------------------------------

Combining the two previous examples will provide for a function that is able
to 


Keyword-only arguments
--------------------------------------------------------------------------------

- Available since: Python v3.0
- PEP-3102: `Keyword-Only Arguments
  <https://www.python.org/dev/peps/pep-3102/>`_
- Motivation: to allow for the declaration of arguments that will only be
  accepted as keyword argument.

  Keyword arguments are usually preferable, since they are explicit and leave
  no room for ambiguity.

Example 1: Function with no positional arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python
   :number-lines: 1
   :class: python-code
   :name: s1_ex01_keyword_only.py

   def xchange(*, amount, from_cur, to_cur):
       xchangerate = {
           ('eur', 'nok'): 10.49,
           ('nok', 'eur'): 0.09540,
           ('usd', 'eur'): 0.8399,
           ('eur', 'usd'): 1.19060,
       }
       return xchangerate.get((from_cur, to_cur)) * amount

- **line 1**: the ``*`` (asterisk) symbol will instruct Python to reject any
  positional arguments starting from its position. In this case: ``*`` is on
  the 1st position, which means that this function will not accept **any**
  positional argument


This works:

.. code:: python
   :class: pycon

   >>> xchange(amount=100, from_cur='eur', to_cur='nok')
   1049.0
   >>> xchange(amount=100, from_cur='eur', to_cur='usd')
   119.06000000000002

But no positional arguments will be accepted:

.. code:: python
   :class: pycon

   >>> xchange(3, from_cur='eur', to_cur='usd')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: xchange() takes 0 positional arguments but 1 positional argument
   (and 2 keyword-only arguments) were given

   >>> xchange(100, 'eur', 'usd')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: xchange() takes 0 positional arguments but 3 were given


Example 2: Function with a non-trivial API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a more elaborate example, where the API design decisions influence the
types of arguments.

The goal of this function argument list is to provide an API with:

- usable defaults,
- no room for ambiguity

.. code:: python
   :name: s1_ex02_miscargs.py
   :number-lines: 1
   :class: python-code

   def room_search2(checkin,
                   *,
                   checkout=None,
                   nr_persons=2,
                   amenities='tv,fridge'):
      if not checkout: checkout=checkin + ' + 1 night'
      print(f'Check-in date: {checkin}')
      print(f'Check-out date: {checkout}')
      print(f'Number of persons: {nr_persons}')
      print(f'Amenities: {amenities}')

- **line 1**: the argument ``checkin`` is the only possible positional
  argument
- **line 2**: only keyword arguments are accepted after the position of the
  ``*`` symbol

**Usage example 1**: only the mandatory first argument is provided

.. code:: python
   :class: pycon

   >>> room_search2('today')
   Check-in date: today
   Check-out date: today + 1 night
   Number of persons: 2
   Amenities: tv,fridge


**Usage example 2**: argument ``3`` is rejected in order to prevent ambiguities
after all the user may mean ``nr_persons=3``, but in this case it would be
interpreted as ``checkout=3``)

.. code:: python
   :class: pycon

   >>> room_search2('today', 3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: room_search2() takes 1 positional argument but 2 were given

**Usage example 3**: the mandatory argument ``"checkin"`` may also be provided as
a keyword argument:

.. code:: python
   :class: pycon

   >>> room_search2(checkin='today')
   Check-in date: today
   Check-out date: today + 1 night
   Number of persons: 2
   Amenities: tv,fridge


.. .. sidebar:: Slide title
..    :subtitle: Slide subtitle
..    :class: slide
..
..    Slide

**Usage example 4**: "Explicite is better than implicit"

Using keyword-arguments only is usually preferable to positional- or mixed
arguments

.. code:: python
   :class: pycon

   >>> room_search2(nr_persons=1, checkin='today')
   Check-in date: today
   Check-out date: today + 1 night
   Number of persons: 1
   Amenities: tv,fridge


Positional-only arguments
-------------------------

- Requires: Python v3.8
- PEP-0570: `Python Positional-Only Parameters
  <https://www.python.org/dev/peps/pep-0570/>`_
- Motivation: as PEP-0570 states: "... flexibility to change the name of positional-only
  parameters without breaking callers."

  That is: choosing descriptive yet intuitive names is becoming increasingly
  difficult. Library authors may change the names of positional-only arguments
  without affecting existing users.


Exercises
================================================================================


.. _ex1:

Exercise 1: Find the problems in this function definition
---------------------------------------------------------

.. code:: python
   :class: pycon

   r = 3
   pi = 3.14

   def circlearea(r=1):
       circlearea = nr ** 2 * pi

   print("The new circle's area is:", circlearea(4))

(See `solution 1 <#sol1>`_)


.. _ex2:

Exercise 2: Define the function ``factorial()``
-----------------------------------------------

(*) Define the function ``factorial()`` with the following specifications:

- it takes a single argument ``n``, which is a positive integer number
- returns the factorial value of ``n``, i.e.: the formula: ``n * n-1 * ...
  * 2 * 1``
- (bonus) make sure that the function only accepts positive integer values
  as the value of ``n``
- (bonus) for invalid input have the function raise a ``TypeError``
  exception

(See `solution 2 <#sol2>`_)



.. _ex3:

Exercise 3(**): Define the function ``daysorter()``
---------------------------------------------------

The function should be able to sort a ``list`` of ``str``'s, where:

- the ``str`` elements are assumed to be the days of the week, e.g.: ::

   l = ['Sun', 'mon', 'TUE', 'sAT', 'Mon', 'Fri', 'wed', 'thU', 
        'WED', 'SUN', 'tue']

- the function will return a new(!) list of the sorted days
- (bonus) make sure that the sorted list will only contain lower-case
  ``str``'s.

Hints:

- the ``sorted()`` function will accept a custom sorting function using the
  ``key=`` argument.

(See `solution03 <#sol3>`_)


.. _ex4:

Exercise 4: Explain!
--------------------------------------------------------------------------------

The following two examples implement the same functionality in two different
ways. Please explain:

- which of these approaches would be preferable and 
- why


.. code:: python
   :number-lines: 1
   :class: python-code

   names = [ 'adele', 'bob', 'cindy', 'doug' ]

   def append(somelist, newelem):
       somelist.append(newelem)
       return somelist

   group = append(names, 'edith')

Solutions
================================================================================


.. _sol1:

Solution 1: Find the problems in this function definition
--------------------------------------------------------------------------------





(go back to `exercise 1 <#ex1>`_)



.. _sol2:

Solution 2: Create the function ``factorial()``
--------------------------------------------------------------------------------




(go back to `exercise 2 <#ex2>`_)



.. _sol3:

Solution 3: (**): Define the function ``daysorter()``
--------------------------------------------------------------------------------



(go back to `exercise 3 <#ex3>`_)





.. vim: filetype=rst textwidth=78 foldmethod=syntax foldcolumn=3 wrap
.. vim: linebreak ruler spell spelllang=en showbreak=… shiftwidth=3 tabstop=3
