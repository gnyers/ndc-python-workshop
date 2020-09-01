================================================================================
Classes: Magic methods to make collection types - Exercises
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
===============================================================================

Sorting with a specific sorting function
--------------------------------------------------------------------------------

**Challenge**
   Sort a list with the days of the week (list of strings) in the correct
   order. ::

    >>> days = 'Mon Sun Tue Fri Sat Sun Mon Tue Mon Wed Sat Thu Fri'.split()
    >>> days
    ['Mon', 'Sun', 'Tue', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Mon', 'Wed', 'Sat', 'Thu', 'Fri']

**Problem**
   By default :func:`sorted()` function will sort strings in alphabetical
   order (lexicographical order). ::

    >>> sorted(days)
    ['Fri', 'Fri', 'Mon', 'Mon', 'Mon', 'Sat', 'Sat', 'Sun', 'Sun', 'Thu', 'Tue', 'Tue', 'Wed']

**Solution**
   Use a sort function which will define the order of the elements: ::

    >>> def day_sorter(day):
    ...     # the desired order of the elements
    ...     order = 'Mon Tue Wed Thu Fri Sat Sun'.split()
    ...     # return the position of the current element in the `order` list
    ...     return order.index(day)
    ...
    >>> sorted(days, key=day_sorter)
    ['Mon', 'Mon', 'Mon', 'Tue', 'Tue', 'Wed', 'Thu', 'Fri', 'Fri', 'Sat', 'Sat', 'Sun', 'Sun']

**Bonus**
   The same sorting function will also work with :func:`min()` and :func:`max()` ::

    >>> min(days)
    Fri                                # No!
    >>> min(days, key=day_sorter)
    Mon                                # Yes!


Counting
--------------------------------------------------------------------------------

.. _dict_persons:

**Challenge**
   How many males and females are in the following :type:`dict`? ::

    persons = [
        {'name': 'Lucy',     'age': 14, 'gender': 'f'},
        {'name': 'Andrej',   'age': 34, 'gender': 'm'},
        {'name': 'Mark',     'age': 17, 'gender': 'm'},
        {'name': 'Thomas',   'age': 44, 'gender': 'm'},
        {'name': 'Evi',      'age': 25, 'gender': 'f'},
        {'name': 'Robert',   'age': 23, 'gender': 'm'},
        {'name': 'Dragomir', 'age': 54, 'gender': 'm'},
        {'name': 'Jenny',    'age': 34, 'gender': 'f'},
        {'name': 'Eline',    'age': 29, 'gender': 'f'},
    ]

**Solution**
   Count the number of values of the :code:`gender` attribute using the
   :type:`collections.Counter` class. **But**: :type:`Counter` needs the
   to be counted values in a sequence-like *Iterable*, e.g.: ::

    >>> from collections import Counter
    >>> Counter('abracadabra')
    Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

   .. _gender_data_iterator:

   **However** the data is in a :type:`dict`! So let's extract the required
   data with a small :code:`lambda` function: ::

    >>> gender_data_iterator = map(lambda v: v['gender'], persons)
    >>> Counter(gender_data_iterator)
    Counter({'m': 5, 'f': 4})

**Bonus**
   What if the data is not clean? ::

    persons2 = [
        {'name': 'Lucy',     'age': 14, 'gender': 'f'},
        {'name': 'Andrej',   'age': 34, 'gender': 'm'},
        {'name': 'Mark',     'age': 17, 'gender': 'M'},
        {'name': 'Thomas',   'age': 44, 'gender': 'M'},
        {'name': 'Evi',      'age': 25, 'gender': 'f'},
        {'name': 'Robert',   'age': 23, 'gender': 'M'},
        {'name': 'Dragomir', 'age': 54, 'gender': 'M'},
        {'name': 'Jenny',    'age': 34, 'gender': 'F'},
        {'name': 'Eline',    'age': 29, 'gender': 'F'},
    ]

   In this case the previous solution clearly would give the wrong answer: ::

    >>> Counter( map(lambda v: v['gender'], persons2) )
    Counter({'M': 4, 'F': 2, 'f': 1, 'm': 1, 'v': 1})

   So, let's lower-case the values before counting: 
   :code:`lambda v: v['gender'].lower()`: ::

    >>> gender_data_iterator2 = map(lambda v: v['gender'].lower(), persons2)
    >>> Counter(gender_data_iterator2)
    Counter({'m': 5, 'f': 4})

   To see how this works, let's examine just the :code:`lambda` function.

   The raw data record: ::
    >>> persons2[3]
    {'name': 'Thomas', 'age': 44, 'gender': 'M'}

   When we apply the :code:`lambda` function to the raw data: ::

    >>> f = lambda v: v['gender'].lower()
    >>> f(persons2[3])
    'm'


Categorizing
--------------------------------------------------------------------------------

**Problem**
   Given the :var:`persons` `(see) <dict_persons_>`_ :type:`dict` of the
   previous example, sort the persons into age groups of decades, that is:
   0-9, 10-19, 20-29, 30-39 etc...

**Analysis**
   Let's define the desired output of our program as a :type:`dict`, where:

   - the keys: are the age buckets, expressed by a :type:`range` object, e.g.:
     :code:`range(10)`. This corresponds with the ages of 0-9.
   - values: are :type:`list`, which contain the persons, who fall in the age
     bucket, e.g.: ::

      {
       range(10, 20): [{'name': 'Lucy', 'age': 14, 'gender': 'f'},
                       {'name': 'Mark', 'age': 17, 'gender': 'm'}],
       range(20, 30): [{'name': 'Evi', 'age': 25, 'gender': 'f'},
                       {'name': 'Robert', 'age': 23, 'gender': 'm'},
                       {'name': 'Eline', 'age': 29, 'gender': 'f'}],
       range(30, 40): [{'name': 'Andrej', 'age': 34, 'gender': 'm'},
                       {'name': 'Jenny', 'age': 34, 'gender': 'f'}]
      }

**Solution**
   We'll need a :type:`list` (or :type:`tuple`), which contains the different
   :type:`range` objects, against which the program will examine a person
   :type:`dict`, e.g.: ::

    categories = (range(9), range(10,20), range(20, 30), range(30, 40))

   Also needed is an empty :type:`dict`, which will store the result: ::

    res = {}

   Finally, a nested loop will walk through the :code:`persons` :type:`dict`
   and match the age of the current :code:`person` against each :type:`range`
   object: ::

    for r in categories:
        for p in persons:
            if p['age'] in r:
                res.setdefault(r, []).append(p)

   The line code:`res.setdefault(r, []).append(p)` is perhaps the most
   intriguing here. Let's break this down:

   - :code:`.setdefault()` method will return one of the following values:

     - the value of the key :code:`r` (i.e.: a :type:`list`), if :code:`r` is
       an existing key in :code:`res`, OR
     - add the key :code:`r` with an empty :type:`list` as value to
       :code:`res` AND return this empty :type:`list` object, if :code:`r` was
       not yet a key

   - in either of the above cases, the expression 
     :code:`res.setdefault(r, [])` will return a :type:`list`, to which we
     append the current person :type:`dict` as a new element.

**Bonus**
   This algorithm will accept any arbitrary age buckets, even if they overlap.
   Observe the extended :code:`categories`, where we added the age groups
   representing: elementary school children, high-school children, adults and
   retirees: ::

    categories = (range(9), range(10,20), range(20, 30), range(30, 40),
                  range(6, 15), range(15, 19), range(19, 67), range(67, 120))

    def categorize(persons, categories):
        res = {}

        for r in categories:
            for p in persons:
                if p['age'] in r:
                    res.setdefault(r, []).append(p)
        return res

    print(categorize(persons, categories))

   The result is: ::

    {range(10, 20): [{'name': 'Lucy', 'age': 14, 'gender': 'f'},
                     {'name': 'Mark', 'age': 17, 'gender': 'm'}],

     range(20, 30): [{'name': 'Evi', 'age': 25, 'gender': 'f'},
                     {'name': 'Robert', 'age': 23, 'gender': 'm'},
                     {'name': 'Eline', 'age': 29, 'gender': 'f'}],

     range(30, 40): [{'name': 'Andrej', 'age': 34, 'gender': 'm'},
                     {'name': 'Jenny', 'age': 34, 'gender': 'f'}],

     range( 6, 15): [{'name': 'Lucy', 'age': 14, 'gender': 'f'}],

     range(15, 19): [{'name': 'Mark', 'age': 17, 'gender': 'm'}],

     range(19, 67): [{'name': 'Andrej', 'age': 34, 'gender': 'm'},
                     {'name': 'Thomas', 'age': 44, 'gender': 'm'},
                     {'name': 'Evi', 'age': 25, 'gender': 'f'},
                     {'name': 'Robert', 'age': 23, 'gender': 'm'},
                     {'name': 'Dragomir', 'age': 54, 'gender': 'm'},
                     {'name': 'Jenny', 'age': 34, 'gender': 'f'},
                     {'name': 'Eline', 'age': 29, 'gender': 'f'}]
    }

Iterable Classes
--------------------------------------------------------------------------------

**Problem**
   Create the :type:`Addressbook` class, which is a collection of
   :type:`Person` instances. Make sure that the :type:`Addressbook` instances
   are *Iterable*.

**Solution**
   Let's use the recently introduced :mod:`dataclasses` module to create the
   classes. ::

    from dataclasses import dataclass, field
    from typing import List


    @dataclass
    class Person:
        fname: str = ''
        sname: str = ''
        gender: str = ''
        email: str = ''

    @dataclass
    class Addressbook:
        name: str = 'My Addressbook'
        _items: List[Person] = field(default_factory=list, init=False)

   At this point the :type:`Addressbook` instances can hold items, but it is
   not yet an *Iterable*: ::

    >>> ab = Addressbook()
    >>> ab
    Addressbook(name='My Addressbook', _items=[])
    >>> ab2._items += [ 'Jenny', 'Robert', 'Alice' ]
    >>> ab2
    Addressbook(name='My Addressbook', _items=['Jenny', 'Robert', 'Alice'])

   However it is not yet an *Iterable*: ::

    >>> list(ab2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'Addressbook' object is not iterable

   In |Python| a class is only *Iterable* if it implements the
   :func:`.__iter__()` method, which provides an *Iterator* instance. So let's
   do it: ::

    @dataclass
    class Addressbook:
        name: str = 'My Addressbook'
        _items: List[Person] = field(default_factory=list, init=False)

        def __iter__(self):
            return iter(self._items)

   It is now working: ::

    >>> ab2 = Addressbook()
    >>> ab2._items += [ 'Jenny', 'Robert', 'Alice' ]
    >>> ab2
    Addressbook(name='My Addressbook', _items=['Jenny', 'Robert', 'Alice'])

    >>> list(ab2)                      # convert Addressbook -> list
    ['Jenny', 'Robert', 'Alice']

   While at it why don't we add a couple of other nice features, such as:

   - implement the :func:`.add()` method, which will add an item to the
     address book
   - implement the :func:`.__len__()` method, so that the :func:`len()`
     function is able to show the number of elements in the collection.

   ::

    @dataclass
    class Addressbook:
        name: str = 'My Addressbook'
        _items: List[Person] = field(default_factory=list, init=False)

        def __iter__(self):
            return iter(self._items)

        def add(self, person):
            self._items.append(person)

        def __len__(self):
            return len(self._items)

   Try out the result: ::

    >>> fred = Person(fname='Fred', sname='Flintstone', gender='m',
                  email='fred@bedrock.place')
    >>> wilma = Person(fname='Wilma', sname='Flintstone', gender='f',
                   email='wilma@bedrock.place')

    >>> ab = Addressbook(name='The Flintstones')
    >>> ab.add(fred)
    >>> ab.add(wilma)

    >>> print(f'Number of entries in addressbook: {len(ab)}')
    2

**Bonus**
   By implementing the :func:`.__getitem__()` magic method on the :type:`Person`
   class, we even can use the `previous solution <gender_data_iterator_>`_ to
   count: ::

    @dataclass
    class Person:
        fname: str = ''
        sname: str = ''
        gender: str = ''
        email: str = ''

        def __getitem__(self, item):
           res = getattr(self, item)
           return res

    @dataclass
    class Addressbook:
        name: str = 'My Addressbook'
        _items: List[Person] = field(default_factory=list, init=False)

        def __iter__(self):
            return iter(self._items)

        def add(self, person):
            self._items.append(person)

        def __len__(self):
            return len(self._items)

    fred = Person(fname='Fred', sname='Flintstone', gender='m',
              email='fred@bedrock.place')

    wilma = Person(fname='Wilma', sname='Flintstone', gender='f',
               email='wilma@bedrock.place')

    ab = Addressbook(name='The Flintstones')
    ab.add(fred)
    ab.add(wilma)

   Finally let's try how our new classes fit in our data-processing toolkit so
   far : ::

    gender_data_iterator = map(lambda v: v['gender'], ab)

    >>> Counter(gender_data_iterator)
    Counter({'m': 1, 'f': 1})


.. vim: filetype=rst textwidth=78 foldmethod=syntax foldcolumn=3 wrap
.. vim: linebreak ruler spell spelllang=en showbreak=… shiftwidth=3 tabstop=3
