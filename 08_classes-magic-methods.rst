================================================================================
Classes: Magic methods to make collection types
================================================================================


.. sectnum::
   :start: 1
   :suffix: .
   :depth: 2

.. contents:: Contents:
   :depth: 2
   :backlinks: entry
   :local:

.. Fancy RST roles, needs rst2html-fancy.css

.. role:: tst
   :class: test
.. role:: file(code)
.. role:: dir(code)
.. role:: key(code)
.. role:: cmd(code)
.. role:: url(code)

.. role:: var(code)
.. role:: type(code)
.. role:: func(code)
.. role:: class(code)
.. role:: mod(code)

.. role:: git(code)
.. role:: commit(code)
.. role:: tag(code)
.. role:: bug(code)

.. role:: app(code)
.. role:: user(code)
.. role:: dottedline(code)
.. role:: verticalspace(code)


.. Abbreviations
.. =============

.. |ANSWER| replace:: **Answer/Solution:**

.. |GIT| replace:: :app:`Git`
.. |PYTHON| replace:: :app:`Python`


.. |DOTTEDLINE| replace:: :dottedline:`✎`


Relevant Magic methods
================================================================================

- Python's Language Specifications define a few dozens  "magic methods", which
  can be used by programmers to integrate their classes into the language.

- The level of integration is quite complete: class authors have the ability
  to seamlessly embed their types into Python. It is even possible to replace
  the type "primitives", such as ``list``, ``dicts`` etc...

In this segment we'll be focusing on implementing the necessary methods to
have a custom class act as a regular collection type:

- ``__iter__()``: integration with ``:func:iter()``
- ``__len__()``: integration with ``:func:len()``
- ``__getitem__``: implements the element lookup notation, e.g.: ``obj[0]``


``__iter__()``
--------------------------------------------------------------------------------

The role of the ``__iter__()`` method:

- Whenever a ``for`` loop, or any of the "Iterator protocol" based tools want
  to process the elements of a collection type, Python will implicitly run
  ``iter(obj)``

- The ``:func:iter()`` function will check for the availability of the
  ``obj.__iter__`` property. If found and it is ``callable``,  the
  ``obj.__iter__()`` method is invoked.

- The expected return value is an ``Iterator`` object, which is able to
  iterate through the elements of ``obj``.

- See also the `Python Language Reference for __iter__()
  <https://docs.python.org/3/reference/datamodel.html#object.__iter__>`_

A minimalistic example for an iterable class:

.. code:: python
   :class: python-code

   class Addressbook:
      def __init__(self, name):
         self.name = name
         self.content = []

      def __iter__(self):
         return iter(self.content)

Another piece of code using the class:

.. code:: python
   :class: python-code

   ab = Addressbook('Personal')
   ab.content.append('Homer')
   ab.content.append('Marge')
   ab.content.append('Bart')
   ab.content.append('Lisa')
   ab.content.append('Maggie')

And finally how to read its content:

.. code:: python
   :class: pycon

   for person in ab:
      print(person)

   Homer
   Marge
   Bart
   Lisa
   Maggie



Since ``ab`` is now an iterable, functions such as ``sorted()``, ``filter()``,
``map()``, ``min()``, ``max()`` etc... would work as expected.


.. code:: python
   :class: pycon

   >>> sorted(ab)
   ['Bart', 'Homer', 'Lisa', 'Maggie', 'Marge']
   >>> list(map(lambda s: s.upper(), ab))
   ['HOMER', 'MARGE', 'BART', 'LISA', 'MAGGIE']

   >>> min(ab)
   'Bart'

   >>> max(ab)
   'Marge'



``__len__()``
--------------------------------------------------------------------------------

The role of the ``__iter__()`` method:

- Whenever ``:func:len(obj)`` is invoked, Python will look for the
  ``obj.__len__`` property. If found and it is ``callable``,  the
  ``obj.__len__()`` method is invoked.

- The expected return value is a positive integer, meaning the number of
  elements in this collection object.

- See also: `Python Language Reference for __len__()
  <https://docs.python.org/3/reference/datamodel.html#object.__len__>`_

Let's implement the ``__len__()`` method for the ``Addressbook`` class:

.. code:: python
   :class: python-code

   class Addressbook:
      def __init__(self, name):
         self.name = name
         self.content = []

      def __iter__(self):
         return iter(self.content)

      def __len__(self):
         return len(self.content)


Following the previous example, this is how this new feature could be
exercised:

.. code:: python
   :class: pycon

   >>> len(ab)
   5


``__getitem__()``
--------------------------------------------------------------------------------

The role of the ``__getitem__()`` method:

- Whenever the element lookup operator ``obj[ ... ]`` is invoked, Python will
  check the availability of the ``obj.__getitem__`` property. If found and it
  is ``callable``,  the ``obj.__getitem__(what)`` method is invoked.

- The ``what`` object depends on the type of collection:

  - a **key**, in case ``obj`` is of a ``dict``-like mapping class, or
  - an **index** or **slice** object, if ``obj`` has a ``list``-like internal
    data structure

- See also: `Python Language Reference for __getitem__()
  <https://docs.python.org/3/reference/datamodel.html#object.__getitem__>`_


Implement ``__getitem__()`` for the ``Addressbook`` class:


.. code:: python
   :class: python-code

   class Addressbook:
      def __init__(self, name):
         self.name = name
         self.content = []

      def __iter__(self):
         return iter(self.content)

      def __len__(self):
         return len(self.content)

      def __getitem__(self, what):
         return self.content.__getitem__(what)

Demo:

.. code:: python
   :class: pycon

   >>> ab[3]
   'Lisa'
   >>> ab[2]
   'Bart'
   >>> ab[0:3]
   ['Homer', 'Marge', 'Bart']
   >>> ab[::-1]
   ['Maggie', 'Lisa', 'Bart', 'Marge', 'Homer']


A bit more advanced use-case, just because we can:

.. code:: python
   :class: pycon

   class Addressbook:
      def __init__(self, name):
         self.name = name
         self.content = []

      def __iter__(self):
         return iter(self.content)

      def __len__(self):
         return len(self.content)

      def __getitem__(self, what):
         if isinstance(what, (int, slice)):
             return self.content.__getitem__(what)
         elif isinstance(what, str):
             return [ e for e in ab if e.find(what) != -1  ]

In addition to everything the previous version did, this one add:

- The argument ``what`` now may be a ``str``
- In this case return all the elements that begin with ``what``


Demo:

.. code:: python
   :class: pycon

   >>> ab['M']
   ['Marge', 'Maggie']
   >>> ab['L']
   ['Lisa']
   >>> ab['H']
   ['Homer']


Exercises
=========

- Ex01: (✪) Create ``BookmarkStash`` class
- Ex02: (✪✪) Extend the ``BookmarkStash``
- Ex03: (✪✪✪) Implement the ``Bookmark`` class

See: `08_classes-magic-methods-exercises.rst
<08_classes-magic-methods-exercises.rst>`_


.. vim: filetype=rst textwidth=78 foldmethod=syntax foldcolumn=3 wrap
.. vim: linebreak ruler spell spelllang=en showbreak=… shiftwidth=3 tabstop=3
