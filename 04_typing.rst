================================================================================
Type Checking
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

Presentation: `Type Checking <https://codesensei.nl/presentations/type-checking-in-python.html>`_


Overview
~~~~~~~~

Type Checking in Python

- What?

- Why?

- How?

- Pros and Cons

Static vs Dynamic
~~~~~~~~~~~~~~~~~

Static Typing (Java, C#, ...)

- Type declarations in code

- Variables are typed

- Function argument types

- Checked statically (compile-time)

Static vs Dynamic
~~~~~~~~~~~~~~~~~

Dynamic Typing (Python, Ruby, JS, ...)

- No type information in code

- No type checking

- Runtime errors

Gradual Typing
~~~~~~~~~~~~~~

The future of Python: *gradual typing*

- (Best of?) both worlds

- Planned for many years

- Support added since python 3.5

PEPs
~~~~

.. table::

    +------+-------------------------------+----------------+
    |  PEP | Topic                         | Python version |
    +======+===============================+================+
    | 3107 | function annotations          |            3.0 |
    +------+-------------------------------+----------------+
    |  484 | type hints                    |            3.5 |
    +------+-------------------------------+----------------+
    |  526 | variable annotations          |            3.6 |
    +------+-------------------------------+----------------+
    |  560 | core support                  |            3.7 |
    +------+-------------------------------+----------------+
    |  561 | stubs                         |            3.7 |
    +------+-------------------------------+----------------+
    |  544 | protocols                     |            3.8 |
    +------+-------------------------------+----------------+
    |  ... | literals, typed dicts, finals |            3.8 |
    +------+-------------------------------+----------------+

The Future Face of Python
-------------------------

Function annotations
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    def average(a: int, b: int) -> float:
        return (a + b) / 2

.. code:: python

    average("a", []) # Still valid python!

- Annotations: PEP 3107

- No formal semantics (use any valid expression)

- Optional; ignored by interpreter

- No effect on runtime (no optimization)

Type annotations
~~~~~~~~~~~~~~~~

.. code:: python

    def average(a: int, b: int) -> float:
        return (a + b) / 2

- Interpretation left to external tools

- Tool examples: mypy, pyre, pytype

- Static type checking before running

Gradual Typing
~~~~~~~~~~~~~~

If you don't add type annotations to a function, the type checker will
not check it!

This allows you to add typing annotations to only parts of your code.

Benefits
~~~~~~~~

Function annotations:

- Document functions

- Allow for static type checking

- Prevent runtime errors

Types and Type Checking
-----------------------

Classes vs Types
~~~~~~~~~~~~~~~~

- A class is a *runtime* concept

- Values are class instances

But a type is a concept for the *checker*

Builtin Classes are Types
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    reveal_type(4)
    reveal_type("hi")
    reveal_type([3,4,5])

.. code:: text

    $ mypy example.py
    1: note: Revealed type is 'builtins.int'
    2: note: Revealed type is 'builtins.str'
    3: note: Revealed type is 'builtins.list[builtins.int*]'

Custom Classes are types
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    class Person:
        ...

    def greet(p: Person) -> str:
        return "Hi " + p.name

List
~~~~

.. code:: python

    from typing import List

    def roots(l: List[int]) -> List[float]:
        return [x**0.5 for x in l]

    print(roots(range(100)))

- There's a typing error in this code..

List 2
~~~~~~

This doesn't work:

.. code:: python

    from typing import List

    def roots2(l: List[int]) -> List[float]:
        return [x**0.5 for x in l.values()]

.. code:: text

    $ mypy list_type.py
    list_type.py:9: error: "List[int]" has no attribute "values"

Mypy knows about class attributes!

Tuples
~~~~~~

.. code:: python

    from typing import Tuple

    x: Tuple[int, str, float] = (3, "yes", 7.5)
    y: Tuple[int, ...] = (5,4,3,2,1)
    z: Tuple[()] = ()

Dicts
~~~~~

.. code:: python

    from typing import Dict, List, Any

    def max_avg(d: Dict[Any, List[float]]) -> float:
        return max([sum(l)/len(l) for l in d.values()])

- ``Dict`` specifies type of key and value

- Note the use of ``Any`` (type, not class)

- ``float`` also implies ``int``

Type Inference
~~~~~~~~~~~~~~

.. code:: python

    def str_len(s: str) -> int:
        return len(s)

    x = str_len("a"), str_len("b")

    reveal_type(x)

.. code:: text

    Revealed type is 'Tuple[builtins.int, builtins.int]'

Type Inference (2)
~~~~~~~~~~~~~~~~~~

.. code:: python

    l = [1,2,3]
    l.append('a') # Can we do this?
    x = 5
    x = []
    z = []

.. code:: text

    error: Argument 1 to "append" of "list" has incompatible type "str"; expected "int"
    error: Incompatible types in assignment (expression has type "List[<nothing>]", variable has type "int")
    error: Need type annotation for 'z' (hint: "z: List[<type>] = ...")

Variable Annotation
~~~~~~~~~~~~~~~~~~~

.. code:: python

    from typing import List

    class Student:
        def __init__(self, name: str) -> None:
            self.name = name
            self.grades: List[int] = []

Types that are NOT Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Any (accept everything)

- Optional

- Union

- (and more...)

Union and Optional
~~~~~~~~~~~~~~~~~~

.. code:: python

    def send_email(address: Union[str, List[str]],
                   sender: str,
                   cc: Optional[List[str]],
                   bcc: Optional[List[str]],
                   subject='',
                   body: Optional[List[str]] = None
                   ) -> bool:
        ...

- ``Optional`` is a ``Union`` with ``None``

Recap
~~~~~

- We can annotate function args and return types

- Variables as well (but these can be inferred)

- All classes are types

- Import types for list, dict etc. from ``typing``

- Use ``Union`` if you accept multiple types


So
~~

You can do many great and complex things with type annotations.

But don't let them fool you: the interpreter ignores them all.

Into the wild
-------------

Using libraries / stdlib
~~~~~~~~~~~~~~~~~~~~~~~~

Demo: requests and stubs

- Stubs are typing annotations kept in ``.pyi`` files, *outside* of the python source

- Mypy comes with its own *typeshed*.

- There are tools to generate stubs (monkeytype, stubgen)

Adding to an existing codebase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Start with most-used/most-imported modules

- Annotate your functions

- Annotate variables only if needed

- Use type checker in CI or pre-commit hook

- Untyped dependencies: create stubs

It's good enough for production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

But you might have some problems

What if you run into problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Use ``Any``

- Use ``typing.cast()``

- ``# type: ignore``

Tools: Mypy
~~~~~~~~~~~

`http://mypy-lang.org/ <http://mypy-lang.org/>`_

Guido van Rossums implementation in Python, most popular.

Tools: Pyre
~~~~~~~~~~~

`https://pyre-check.org/ <https://pyre-check.org/>`_

- Created by Facebook

- Written in ocaml

- High performance on large code bases

- No Windows support

Tools: Pytype
~~~~~~~~~~~~~

`https://github.com/google/pytype <https://github.com/google/pytype>`_

- Created by google

- Written in python

- Different philosophy: uses inference instead of gradual typing.

- Lenient instead of strict.

pyright (microsoft)
~~~~~~~~~~~~~~~~~~~

`https://github.com/Microsoft/pyright <https://github.com/Microsoft/pyright>`_

- Created by MicroSoft

- Written in TypeScript (no dependency on python)

- Fast

- VS Code integration

Things to love
--------------

- Clean syntax

- Protocols are great

- Gradual Typing is wonderful

- Documentation and correctness testing

- Better productivity, maintainability

- Great for large/complex projects

But..
-----

Users from other languages
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    def foo(x: int) -> str:
        # x does not have to be an int here!

- Wrong impression for users from java, C#

- Same with @overload, TypeVar

Preferable?
~~~~~~~~~~~

.. code:: python

    def foo(x):
        # type: int -> str

That's it
---------

Now go and add type annotations to your code!
