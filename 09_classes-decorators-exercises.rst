================================================================================
Classes: class- and static methods, properties - Exercises
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

See also: the `solutions <09_classes-decorators-exercises-solutions.py>`_


Ex01: (✪✪) Create the ``BookmarkStash.from_csv`` class method
------------------------------------------------------------

Specifications:

- Given the following content in a `CSV <09_ex01.csv>`_ file, the
  ``.from_csv()`` method should create a new ``BookmarkStash`` instance: ::

   name;url
   Python Home;https://www.python
   Google Search Engine;https://google.com
   Github;https://github.com

- The ``.from_csv()`` method should accept the following arguments:

  - ``fname``: name of the CSV file
  - ``name``: name of the new ``Bookmarkstash`` instance, default value:
    ``Imported Bookmarkstash``
  - ``delim``: optional, default value ``;``

- Implement the ``BookmarkStash.__str__()`` magic method such, that the
  its instances will look something similar: ::

   >>> bm = BookmarkStash(name='My Bookmarks')
   >>> bm.add(Bookmark(name='Python Home', url='https://python.org'))
   >>> bm.add(Bookmark(name='GitHub', url='https://github.com'))
   >>> print(bm)
   My Bookmarks (2)

**Hints**:

- You may consider the ``csv`` module, but in this case the ``.split(';')``
  method will do fine
- to open this CSV file you'll need something like: ::

   >>> bm_csv = open('09_ex01.csv', 'rt').read()
   >>> type(bm_csv)
   <class 'str'>


Ex02: (✪) Create the ``Bookmark.validate_url`` static method
------------------------------------------------------------------

Specifications:

- Based on the ``Bookmark`` class of the previous segment's  "Ex03"
- The method will take a single ``str`` argument: ``url``
- The return value is always a boolean; ``True`` if the provided ``str`` looks
  like a valid URL; ``False`` if not

- Implement the appropriate checks according to these examples:

  - 'http://python.org': OK
  - 'https://python.org': OK
  - 'http:://python.org': NOT OK (too many ':')
  - 'http:/python.org': NOT OK (missing 2nd '/')
  - 'https://python': NOT OK (domain needs at least 2 parts)
  - 'http://python.org.42': NOT OK (TLD may not contain only digits)


**Hints**:

- The required checks are challenging, but you can implement them using only
  the ``.split()``, ``.find()``, ``.count()`` and other ``str`` methods and
  list splicing techniques

- If you prefer, you may use Python's ``re`` module, that implements Regular
  Expressions. You could use the following lines of code: ::

   regex = r'(https?)://([a-zA-Z0-9.]+):?([0-9]*)(/?.*$)'
   parts = re.match( regex, url)
   prot, domain, portnr, pageurl = parts.groups()

  Extra info on RegEx: it will split the URL into 4 parts ::

     Example URL:    'https://python.org:3333/asdf/asdf'
     Parts:           | 0  |  |    1   | | 2||   3     |
                      `----'  `--------' `--'`---------'

  Where:
  - 0: protocol
  - 1: domain
  - 2: port nr (optional)
  - 3: page URL


Ex03: (✪✪✪) Create the ``BookmarkStash.valid_bookmarks`` property
-----------------------------------------------------------------

Specifications:

- This is a read-only property
- The property should return a ``list`` of ``Bookmark`` objects that are validated an on-line


**Hints**:

- To check the availability of an URL, you may use the following snippet: ::

   >>> import urllib.request   
   >>> conn = urllib.request.urlopen('http://python.org')
   >>> type(conn)
   <class 'http.client.HTTPResponse'>

  If the URL is invalid, you will get a lengthy exception: ::

   >>> conn = urllib.request.urlopen('http://python.org')
   ...
   ...  lots of exception traceback info
   ...
   urllib.error.URLError: <urlopen error [Errno -2] Name or service not known>



.. vim: filetype=rst textwidth=78 foldmethod=syntax foldcolumn=3 wrap
.. vim: linebreak ruler spell spelllang=en showbreak=… shiftwidth=3 tabstop=3

