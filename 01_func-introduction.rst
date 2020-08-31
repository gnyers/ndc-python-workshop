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


Recap
================================================================================

.. figure:: ./images/01_func_function_in_out.svg
   :width: 80%
   :alt: a function is a black box

   A Python function takes arguments as input and returns a single object

Functions:

- are callable objects: they represent one or more statements
- the purpose of functions is to be able to re-use these statements all over
  our program(s)
- can take a fixed or variable number of arguments
- can take a function as argument and return a function (also known as:
  "first-class" functions)

Declaring functions
================================================================================

Using the ``def`` keyword
--------------------------------------------------------------------------------

The primary syntax to define functions.

**Example**:

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

**Typical example of a lambda functions**:

- The elements of list ``team`` are mixed-case strings

   .. code:: python
      :class: pycon

      >>> team
      ['evE', 'ALEX', 'joe', 'dAn', 'Oli']

- Sorting such a list is not trivial, especially if we must preserve the case

   .. code:: python
      :class: pycon

      >>> sorted(team)
      ['ALEX', 'Oli', 'dAn', 'evE', 'joe']

- The ``"sorted()"`` function's ``"key="`` argument is provided with
  a callable object defined as a lambda function: ``lambda n: n.lower()``.


   .. code:: python
      :class: pycon

      >>> sorted(team, key=lambda n: n.lower())
      ['ALEX', 'dAn', 'evE', 'joe', 'Oli']


- The ``lambda`` function is usually no longer needed after such an operation


Return value
================================================================================

- Python functions return exactly one object
- By default all functions return the ``None`` object,

  .. code:: python
     :class: python-code

     def f(a, b):
         print(a, b)

     return_value = f('age', 42)

  the value of ``return_value`` is ``None``!

- The default ``None`` return object can be *overridden* by a ``return``
  statement:

  .. code:: python
     :class: python-code

     def f(a, b):
         print(a, b)
         return 42

     return_value = f('age', 42)

  the value of ``return_value`` is now ``42``!

- To return multiple values, put them all into some collection object, e.g. a
  ``tuple``:

  .. code:: python
     :class: python-code

     def f(a, b, c):
         return c, b, a

     return_value = f('Homer', 'Bart', 'Marge')

  the value of ``return_value`` is ``('Marge', 'Bart', 'Homer')``!


- The ``return`` statement will evaluate the result its expression:

  .. code:: python
     :class: python-code

     def c2f(celsius, /):
         return celsius * 9 / 5 + 32

     temp_f = c2f(24)

- If the function has more than one ``return`` statements, the return value
  will be determined by whichever is evaluated first:

  .. code:: python
     :class: python-code

     def agecategory(age):
         if     0  <  age < 12 : return 'child'
         elif   12 <= age < 18 : return 'teen'
         elif   18 <= age < 67 : return 'adult'
         elif   67 <= age < 120: return 'senior'
         else                  : return 'No!'



Fuction arguments
================================================================================

Argument passing
--------------------------------------------------------------------------------

Argument passing to functions in Python is a bit unusual compared to other
programming languages. In this context, the usual terms ``by-reference`` and
``by-value`` do not apply for Python.

Example
^^^^^^^

.. code:: python
   :class: python-code

   name = 'Sponge Bob'
   pals = ['Patrick', 'Sandy', 'Gary']

   def mixup(character, friends):
       character = 'Mr. Krabs'
       friends.clear()

   mixup(name, pals)
   print(f'Character name: {name}')
   print(f"Character's fiends: {pals}")

- When executed, the above example will print: ::

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

Even if the arguments are collection objects:

.. code:: python
   :class: pycon

   >>> add((1,2,3), (4,))
   (1, 2, 3, 4)


Optional arguments
--------------------------------------------------------------------------------

If an argument is assigned a default value, that argument may be omitted when
calling the function.

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


Providing arguments when calling functions
================================================================================

There are two possible notations for an argument to be passed to a function:

.. code:: python
   :class: python-code

   def add(a,b):
       print(f'arg "a": {a}')
       print(f'arg "b": {b}')
       return a + b

#. as a positional argument:

   .. code:: python
      :class: pycon

      >>> add(2, 3)
      arg "a": 2
      arg "b": 3
      5

   In this example argument ``"a"`` has been assigned the object ``2``, and
   ``"b"`` got ``3``.

   The reason for this is the position of resp. ``"a"`` and ``"b"`` on the
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
"Explicit is better than implicit"


Functions with variable number of arguments
================================================================================

It is sometimes useful when a function is able to consume a variable number of
arguments.

**Example**: the ``print()`` function!

Variable number of positional arguments
--------------------------------------------------------------------------------

**Example**:

.. code:: python
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

**Note the limitation**: the function ``greet()`` can only process positional
arguments:

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
   :class: python-code

   def show(**attributes):
      for attr in attributes:
          print(f'{attr} = {attributes[attr]}')

The notation ``**attributes`` will instruct Python to collect every positional
arguments into a ``dict`` and assign it to the variable ``attributes``.


**Note the limitation**: the function ``attributes()`` can only process
keyword arguments!


Variable number of postional and keyword arguments
--------------------------------------------------------------------------------

Combining the two previous examples will provide the possibility to create
functions, which can consume a variable number of arguments, both as
positional as well as keyword arguments:


.. code:: python
   :class: python-code

   def generic(*args, **kwargs):
       for nr, arg in enumerate(args):
           print(f'Positional arg {nr}: {arg}')
       for key, value in kwargs.items():
           print(f'Keyword arg {key}: {value}')


**Example usage 1**: just invoke ``generic()`` with a bunch of arguments

   .. code:: python
      :class: pycon

      >>> generic('red', 'green', 'blue', name='Homer', age=42)
      Positional arg 0: red
      Positional arg 1: green
      Positional arg 2: blue
      Keyword arg name: Homer
      Keyword arg age: 42

**Example usage 2**: the order of argument types is important: **first** all positional arguments and **then**: all keyword arguments!

   .. code:: python
      :class: pycon

      >>> generic('red', color='green', 'blue', name='Homer', age=42)
        File "<stdin>", line 1
      SyntaxError: positional argument follows keyword argument


Enforcement of how users provide arguments (*)
================================================================================

It is sometimes useful for function authors to enforce a particular way to
provide arguments when calling the function, e.g.:

- users of a function must **always** use keyword arguments, to have the
  freedom of changing the function's signature, if it is not yet finalized:

  today: ``def bookroom(nr_persons, checkin, checkout):``

  tomorrow: ``def bookroom(checkin, checkout, nr_persons, amenities):``

- users should **always** use positional arguments, in order to be free (as
  function authors) to change the argument names:

  today: ``def c2f(temp):``

  tomorrow: ``def c2f(celsius):``


Keyword-only arguments
--------------------------------------------------------------------------------

- Available since: Python v3.0
- PEP-3102: `Keyword-Only Arguments
  <https://www.python.org/dev/peps/pep-3102/>`_

Example 1: Function with no positional arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python
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
--------------------------------------------------------------------------------

- Requires: Python v3.8
- PEP-0570: `Python Positional-Only Parameters
  <https://www.python.org/dev/peps/pep-0570/>`_
- Motivation: as PEP-0570 states: "... flexibility to change the name of positional-only
  parameters without breaking callers."

  That is: choosing descriptive yet intuitive names is becoming increasingly
  difficult. Library authors may change the names of positional-only arguments
  without affecting existing users.


Example 1: Function with only positional arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python
   :name: filename.py
   :class: python-code

   def f2c(farenheid, /):
       return 5 / 9 * (farenheid - 32)

   def c2f(celsius, /):
       return celsius * 9 / 5 + 32


**Usage example 1**: calling the functions with positional arguments will work
correctly:

.. code:: python
   :class: pycon

   >>> c2f(20)
   68.0
   >>> f2c(68)
   20.0


**Usage example 2**: trying to invoke the functions with keyword arguments
will fail:


.. code:: python
   :class: pycon

   >>> c2f(celsius=20)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: c2f() got some positional-only arguments passed as keyword arguments: 'celsius'

   >>> f2c(farenheid=68)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: f2c() got some positional-only arguments passed as keyword arguments: 'farenheid'

- Note that Python recognizes the ``celsius`` and ``farenheid`` arguments, but
  because they are positional-only arguments, it will throw an exception!





Summary
================================================================================

In this segment we've walked through the basics of defining and using
functions in Python.

- Function can be defined using the ``def`` and ``lambda`` keywords.
- Python has first-class functions, i.e.: functions may be called with
  functions as arguments.
- When calling functions, it is recommended to use the keyword-argument
  notation, because it is explicit.
- Python also provides a rich notation to define the way how arguments may be
  provided when calling a function, i.e.:

  - ``def varargs(*args, **kwargs):`` : variable number of arguments, that may
    be provided both as positional as well as keyword arguments

  - ``def posargsonly(arg1, arg2, /):`` : only positional arguments
  - ``def kwargsonly(*, kwarg1, kwarg2):`` : only keyword arguments allowed

What we haven't talked about are:

- namespaces (isolation of variable names)
- the scoping rule (the order in which Python will look through different
  namespaces when searching for a variable: local -> enclosing -> global ->
  builtin)



.. vim: filetype=rst textwidth=78 foldmethod=syntax foldcolumn=3 wrap
.. vim: linebreak ruler spell spelllang=en showbreak=… shiftwidth=3 tabstop=3
