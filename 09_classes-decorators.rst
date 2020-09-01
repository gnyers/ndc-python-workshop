================================================================================
Classes: class and static methods, properties 
================================================================================


.. sectnum::
   :start: 1
   :suffix: .
   :depth: 2

.. contents:: Contents:
   :depth: 2
   :backlinks: entry
   :local:


In this segment we will be examining a few decorators, which are often used
for classes:

- ``@classmethod``: often used as alternative constructors for instances.
  All ``@classmethod`` are available immediately from the class itself,
  whithout the need to create an instance first

- ``@staticmethod``: often we wish to "package" utilitarian methods with our
  classes, which otherwise do not relate to instance- or class properties

- ``@property``: 

``@classmethod``
================================================================================

``@classmethod``:

- is often used as an alternative constructor, e.g. to create a new instance
  from a data structure

- is part of Python's ``builtins`` module, i.e.: it is always loaded during
  the initialization of the interpreter itself

- is a function, that can be used as a decorator (i.e.: it both takes and
  returns a function)

- will modify the class' internals, overriding the internal data structure of
  the class.

  In the context of a class, an undecorated function object will normally
  become an instance method. Use as a decorator, ``classmethod`` will
  override this mechanism and transform the function into a class method.

  The main difference being the first positional argument: instead of pointing
  to an instance, it refers to the class itself.

A minimalistic example: ``.from_dict()``
----------------------------------------

.. code:: python
  :number-lines: 1
  :class: python-code

  class Contact:
     def __init__(self, name):
         # this is the constructor of new instances
         self.name = name

     @classmethod
     def from_dict(cls, attributes):
         # this method can be used as an alternative constructor
         # for new instances
         contact = cls(attributes.pop('name'))
         for prop, value in attributes.items():
             # create the attributes for ``contact``
             setattr(contact, prop, value)
         return contact

- **line 2**: the class' normal constructor, which will be automatically
  executed upon creation of a new instance.

  **Note**: the argument ``self`` will be automatically filled in by
  Python and points to the newly created class object.

- **line 6**: the ``@classmethod`` decorator will convert ``from_dict`` from
  an instance method to a class method, the consequences of which are:

  - ``from_dict`` will be immediately available as a class property:
    ``Contact.from_dict``
  - the 1st argument of ``from_dict`` will be automatically filled in and
    point to the class itself.

- **line 10**: we create a new instance of ``Contact`` by taking the ``name``
  element from the ``attributes``

  **Note**: ``cls`` is a variable pointing to the ``Contact`` class

- **line 11 - 13**: take the "bag" of attributes, that is the ``properties``
  dictionary and add each ``attribute`` - ``value`` pair to the instance

- **line 14**: we return the newly created instance of ``Contact``

Usage example:

.. code:: python
   :class: pycon

   # A ``dict`` containing the properties of the new Contact
   >>> joe_attrs = dict(name='Joe', email='joe@example.com', company='Acme CO')

   >>> joe = Contact.from_dict(joe_attrs)

- The dictionary ``joe_attrs`` contains all the new contact's attributes
- ``joe`` is a variable pointing to the new ``Contact`` instance

Verify:

.. code:: python
   :class: pycon

   >>> type(joe)
   <class '__main__.Contact'>

   >>> joe.name
   'Joe'

@staticmethod
================================================================================

The ``@staticmethod`` decorator:

- is often used to "package" utilitarian methods with our classes, which
  otherwise do not relate to instance- or class properties

- is part of Python's ``builtins`` module, i.e.: it is always loaded during
  the initialization of the interpreter itself

- is a function, that can be used as a decorator (i.e.: it both takes and
  returns a function)

- will modify the class' internals, overriding the internal data structure of
  the class.

A minimalistic example: ``.from_dict()``
----------------------------------------

.. code:: python
  :number-lines: 1
  :class: python-code

   class Contact:
      def __init__(self, name):
         # this is the constructor of new instances
         self.name = name

      @staticmethod
      def verify_email(email):
          name, *domain_l = email.split('@')
          if len(domain_l) != 1: return False
          domain = domain_l[0]
          domainparts = domain.split('.')
          if len(domainparts) < 2: return False
          return True


- **line 2**: the class' normal constructor, which will be automatically
  executed upon creation of a new instance.

  **Note**: the argument ``self`` will be automatically filled in by
  Python and points to the newly created class object.

- **line 6**: the ``@classmethod`` decorator will convert ``verify_email`` from
  an instance method to a static method, the consequences of which are:

  - ``verify_email`` will be immediately available as a class property:
    ``Contact.verify_email``
  - none of the method's arguments will be automatically filled in by Python
    (as opposed to the instance- and class methods)

- **line 7**: Note the argument list of the method: no ``self`` or ``cls``.
  The regular rules of function arguments do apply without exception.

- **lines 8 - 11**: do different check to determine if the ``email`` string is
  a valid email address.


Usage example:

.. code:: python
   :class: pycon

   >>> Contact.verify_email('joe@example.com')
   True

   >>> Contact.verify_email('joe@example')        # b/c of line 11
   False

   >>> Contact.verify_email('joe@example.com@')   # b/c of line 9
   False

   >>> Contact.verify_email('joe.example.com')    # b/c of line 9




@property
================================================================================

The ``@property`` decorator:

- is used to create a data attribute, whose value is being calculated
  on-demand

- is part of Python's ``builtins`` module, i.e.: it is always loaded during
  the initialization of the interpreter itself

- is a function, that can be used as a decorator (i.e.: it both takes and
  returns a function)

- will modify the class' internals, overriding the internal data structure of
  the class.


A minimalistic example: ``.fullname``
-------------------------------------

First let's compare and contrast between a **static** data attribute and
a **dynamicaly** calculated property.

Level 0: static properties
^^^^^^^^^^^^^^^^^^^^^^^^^^

An example for a **static** data attribute:

.. code:: python
  :number-lines: 1
  :class: python-code

  class Contact:
      def __init__(self, fname, sname):
          # this is the constructor of new instances
          self.fname = fname
          self.sname = sname
          self.fullname = f'{fname}, {sname}'

Level 1: semi-dynamic properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The same property implemented with a **setter** method:

.. code:: python
  :class: python-code

  class Contact:
    def __init__(self, fname, sname):
        # this is the constructor of new instances
        self.fname = fname
        self.sname = sname
        self.set_fullname()

    def set_fullname(self):
        self.fullname = f'{self.sname}, {self.fname}'


Usage example:

.. code:: python
   :class: pycon

   >>> joe = Contact('Joe', 'Smith')
   >>> joe.fullname
   'Smith, Joe'

   >>> joe.fname = 'John'          # change a data attribute
   >>> joe.fname                   # verify the change
   'John'

   >>> joe.fullname
   'Smith, Joe'                    # Oops! fullname attribute is not correct


   >>> joe.set_fullname()          # We can recover, but it is an extra step
   >>> joe.fullname
   'Smith, John'


Level 2: (read-only) dynamic properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python
  :number-lines: 1
  :class: python-code

   class Contact:
       fullname_format = '{sname}, {fname}'
       def __init__(self, fname, sname):
           # this is the constructor of new instances
           self.fname = fname
           self.sname = sname

       @property
       def fullname(self):
           return self.fullname_format.format(**self.__dict__)

- **line 2**: we've added a class variable, which will be shared amongst all
  the instances. In this case we'll use it for the formatting of the
  ``fullname`` attribute

- **line 10**: a bit of an aside: let's unpack the ``**self.__dict__``
  expression:

  - most objects in Python have a ``.__dict__`` property, that is a ``dict``
    and contains all the object's attributes as keys and their values. So does
    the ``joe`` object: ::

     >>> joe.__dict__
     {'fname': 'John', 'sname': 'Smith'}

  - the ``**`` (double asterisk) notation can be used to unpack a ``dict``
    type to keyword arguments. So when calling the ``.format()`` method, in
    effect Python executes this:

     '{sname}, {fname}'.format(fname='John', sname='Smith')


Usage example:

.. code:: python
   :class: pycon

   >>> joe = Contact('Joe', 'Smith')
   >>> joe.fullname
   'Smith, Joe'

   >>> joe.fname = 'John'          # let's change the Firstname property
   >>> joe.fullname                # Full name is immediately "updated"
   'Smith, John'

Note that ``fullname`` is not a "proper" attribute (yet!):

.. code:: python
   :class: pycon

   >>> joe.fullname = 'asdf'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: can not set attribute



A more advanced example: read-write ``.fullname``
-------------------------------------------------

In this section will add the following new features:

- the ability to read and write the ``.fullname`` attribute
- data validation

.. code:: python
  :number-lines: 1
  :class: python-code

   class Contact:
       fullname_format = '{sname}, {fname}'
       def __init__(self, fname, sname):
           # this is the constructor of new instances
           self.fname = fname
           self.sname = sname

       @property
       def fullname(self):
           fullname = getattr(self, '_fullname', None)
           if fullname:
               return self._fullname
           else:
               return self.fullname_format.format(**self.__dict__)

       @fullname.setter
       def fullname(self, name):
           if isinstance(name, str) and name:
               self._fullname = name
           else:
               raise ValueError('I need a string here!')

- **line 8**: the ``@property`` decorator will create a new object
  ``fullname``
- **line 10**: figure out if the instance already has the ``_fullname`` hidden
  attribute set.
- **line 12**: if the instance has a ``_fullname`` attribute, return that
- **line 14**: if no specific ``_fullname`` attribute set, return the full
  name using the formatting defined in the class
- **line 16+17**: designate this method as the one, which will be called, if
  the property is being changed to the value provided in ``name``
- **line 18**: validate input
- **line 21**: if we're not satisfied with the provided new value, we raise an
  exception

Usage example:

.. code:: python
   :class: pycon

   >>> joe = Contact('Joe', 'Smith')
   >>> joe.fullname
   'Smith, Joe'

   >>> joe.fullname = 42           # Integer values will not work!
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "x.py", line 81, in fullname
       raise ValueError('I need a string here!')
   ValueError: I need a string here!

   >>> joe.fullname = ''           # Neither will an empty string do!
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "x.py", line 81, in fullname
       raise ValueError('I need a string here!')
   ValueError: I need a string here!


Summary
================================================================================

- The decorators ``@classmethod``,  ``@staticmethod`` and ``@property`` are
  practical examples of the added value of decorators

- Decorators will allow for the separation of concern, i.e.: the programmer
  can focus on implementing the actual goal that needs to be achieved, instead
  of worrying about how the class internals need to modified.

- ``@classmethod``: allows for multiple alternative constructors -- amongst others

- ``@staticmethod``: allows for handy functions to be "packaged" as methods
  into a class

- ``@property``: though Python does not enforce Encapsulation, but the
  ``@property`` decorator allows for something similar.


Exercises
=========

See `09_classes-decorators-exercises.rst <09_classes-decorators-exercises.rst>`_


.. vim: filetype=rst textwidth=78 foldmethod=syntax foldcolumn=3 wrap
.. vim: linebreak ruler spell spelllang=en showbreak=… shiftwidth=3 tabstop=3
