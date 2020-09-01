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
================================================================================

Ex01: (✪) Create ``BookmarkStash`` class
-------------------------------------

With the following specifications:

- Data attributes:

  - ``owner``: the person who's the owner of this stash
  - ``elements``: a collection of Bookmarks

- Make sure that it is possible to process all ``Bookmark``s objects using the
  ``map()`` function.
- The ``len()`` function must be able to read the number of elements
- Implement the required methods that are required in the "Example usage"
  demo.


**Example usage**:

.. code:: python
   :class: pycon

   >>> bm = BookmarkStash(name="Work")
   >>> bm.add('https://python.org')
   >>> bm.add('https://w3.org')
   >>> bm.add('https://pypi.org')
   >>> print(bm)
   'BookmarkStash with 2 objects'


**Hint**: you'll need to implement the following methods: ``.__str__``,
``.__iter()``, ``.__len__()``


Ex02: (✪✪) Extend the ``BookmarkStash``
---------------------------------------

as follows:

- the container should only hold unique URLs, so no duplicates
- (Optional) when listing the content, the order of the listing should retain the order
  in which the Bookmarks have been added to the ``BookmarkStash``
- implement a search feature using the element lookup operator, i.e.:
  ``stash['python']`` should return all Bookmarks, whose URL contains the
  word ``python``.


Ex03: (✪✪✪) Implement the ``Bookmark`` class
-------------------------------------------

With the following specifications:

- It should store the following information: ``url``, the ``date`` when it was
  added and a list of ``keywords``
- Make sure that the ``BookmarkStash`` class provides for a search method to
  find all ``Bookmark`` objects that are related to a keyword




.. vim: filetype=rst textwidth=78 foldmethod=syntax foldcolumn=3 wrap
.. vim: linebreak ruler spell spelllang=en showbreak=… shiftwidth=3 tabstop=3
