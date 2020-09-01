#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
print('\n\n' + '=' * 78)
print('# Ex01: (✪) Create ``BookmarkStash`` class')
class BookmarkStash:
    def __init__(self, name):
        self.name = name
        self.content = []

    def add(self, url):
        self.content.append(url)

    def __iter__(self):
        return iter(self.content)

    def __str__(self):
        return '{} ({})'.format(self.name, len(self.content))

    def __len__(self):
        return len(self.content)

bm = BookmarkStash(name="Work")
bm = BookmarkStash(name="Work")
bm.add('https://python.org')
bm.add('https://w3.org')
bm.add('https://pypi.org')
print(bm)
print('## Test: loop through all elements:')
for e in bm:
    print(e)

# -------------------------------------------------------------------
print('\n\n' + '=' * 78)
print('# Ex02: (✪✪) Extend the ``BookmarkStash``')

class BookmarkStash:
    def __init__(self, name):
        self.name = name
        self.content = []

    def add(self, url):
        if url in self.content:
            raise ValueError('Already there: {}'.format(url))
        else:
            self.content.append(url)

    def __iter__(self):
        return iter(self.content)

    def __str__(self):
        return '{} ({})'.format(self.name, len(self.content))

    def __len__(self):
        return len(self.content)

    def __getitem__(self, what):
        if isinstance(what, (int, slice)):
            return self.content.__getitem__(what)
        elif isinstance(what, str):
            return [ e for e in self.content if e.find(what) != -1  ]

bm = BookmarkStash(name="Work")
bm = BookmarkStash(name="Work")
bm.add('https://python.org')
bm.add('https://w3.org')
bm.add('https://pypi.org')

print('##-- Test: element lookup by index:')
print(bm[0])

print('##-- Test: slicing:')
print(bm[0:2])

print('##-- Test: how many elements?')
print(len(bm))

print('##-- Test: element lookup by search str')
print(bm['python'])

#print('##-- Test(fail): do not allow duplicates!')
#bm.add('https://w3.org')


# -------------------------------------------------------------------
print('\n\n' + '=' * 78)
print('# Ex03: (✪✪✪) Implement the ``Bookmark`` class')

import time

class Bookmark:
    def __init__(self, url):
        self.url = url
        self.date = time.localtime()  # <<<<< get the current time and date

    def __str__(self):     # 2nd bullet of Ex03
        return self.url

    def __repr__(self):
        return 'Bookmark("{}")'.format(self.url)

class BookmarkStash:
    # to support searching by the URL value we do a simple change
    # in the BookmarkStash.__getitem__() method
    def __init__(self, name):
        self.name = name
        self.content = []

    def add(self, bookmark):
        # we want only Bookmark instances and no duplicates
        if not isinstance(bookmark, Bookmark):
            raise ValueError('Need a Bookmark instance, got: {}'.format(type(bookmark)))
        if bookmark.url in self.content:
            raise ValueError('No duplicates! ({})'.format(bookmark.url))
        self.content.append(bookmark)

    def __iter__(self):
        return iter(self.content)

    def __str__(self):
        return '{} ({})'.format(self.name, len(self.content))

    def __len__(self):
        return len(self.content)

    def __getitem__(self, what):
        if isinstance(what, (int, slice)):
            return self.content.__getitem__(what)
        elif isinstance(what, str):
            # required change for 2nd bullet Ex03---v
            return [ e for e in self.content if str(e).find(what) != -1  ]

bm = BookmarkStash(name="Work")
bm.add(Bookmark('https://python.org'))
bm.add(Bookmark('https://w3.org'))
bm.add(Bookmark('https://pypi.org'))


print('##-- Test: Bookmark element attributes:')
b = bm[0]
print(b.url, b.date)

print('##-- Test: Bookmark lookup:')
print('     using slicing:', bm[:2])
print('     using str:', bm['python'])

print('##-- Test: Optional: Bookmark representation:')
print(repr(b))

# print('##-- Test(fail): only allow Bookmark instances !')
# bm.add('https://w3.org')

# print('##-- Test(fail): do not allow duplicates!')
# bm.add(Bookmark('https://pypi.org'))


