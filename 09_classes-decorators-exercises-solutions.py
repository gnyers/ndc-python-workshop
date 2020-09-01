#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# -------------------------------------------------------------------
print('\n\n' + '=' * 78)
print('# Ex01: (✪✪) Create the ``BookmarkStash.from_csv`` class method')

import time

class Bookmark:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.date = time.localtime()

    def __str__(self):
        return self.url

    def __repr__(self):
        return 'Bookmark("{}", "{}")'.format(self.name, self.url)

class BookmarkStash:
    def __init__(self, name):
        self.name = name
        self.content = []

    def add(self, bookmark):
        if isinstance(bookmark, Bookmark) and bookmark.url not in self.content:
            self.content.append(bookmark)
        else:
            raise ValueError('Already there: {}'.format(bookmark.url))

    @classmethod
    def from_csv(cls, fname, name='Imported Bookmarkstash', delim=';'):
        try:
            # read file content
            bm_csv_l = open(fname, 'rt').readlines()
        except FileNotFoundError:
            print('Can not open {}'.format(fname))
            raise           # re-raise exception

        stash = cls(name)
        for rec in bm_csv_l[1:]:      # 1st line is header, skip!
            name, url = rec.strip().split(delim)
            bm = Bookmark(name, url)
            stash.add(bm)
        return stash

    def __iter__(self):
        return iter(self.content)

    def __str__(self):
        return '{} ({})'.format(self.name, len(self.content))

    def __repr__(self):
        return '<BookmarkStash "{}">'.format(self.__str__())

    def __len__(self):
        return len(self.content)

    def __getitem__(self, what):
        if isinstance(what, (int, slice)):
            return self.content.__getitem__(what)
        elif isinstance(what, str):
            # required change for 2nd bullet Ex03---v
            return [ e for e in self.content if str(e).find(what) != -1  ]


print('## Test: Import bookmarks from CSV:')
bmcsv = BookmarkStash.from_csv('09_ex01.csv')
print(bmcsv)

print('## Test: loop through all elements:')
for e in bmcsv:
    print(e)

# -------------------------------------------------------------------
print('\n\n' + '=' * 78)
print('# Ex02: (✪✪) Create the ``Bookmark.validate_url`` static method')

import re
class Bookmark:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.date = time.localtime()

    def __str__(self):
        return self.url

    def __repr__(self):
        return 'Bookmark("{}", "{}")'.format(self.name, self.url)

    @staticmethod
    def validate_url(url):
        # check 0
        if url.count('.') < 1:
            print('Invalid URL: not enough domain parts')
            return False
        if url.count(':') < 1:
            print('Invalid URL: need a protocol')
            return False
        if url.count('/') < 2:
            print('Invalid URL')
            return False

        # Use a regex to validate URL
        regex = r'(https?)://([a-zA-Z0-9.]+):?([0-9]*)(/?.*$)'
        parts = re.match(regex, url)
        if not parts:
            print('Invalid URL: ')
            return False

        prot, domain, portnr, pageurl = parts.groups()
        print('DEBUG:', parts.groups())
        domainparts = domain.split('.')
        if len(domainparts) < 2:
            print('Invalid URL: not enough domain parts')
            return False

        # check TLD for digits-only
        if domainparts[-1].isdigit():
            print('Invalid URL: domain TLD may not conain only digits')
            return False

        return True

print('##-- Test(True): http://python.org')
print(Bookmark.validate_url('http://python.org'))

print('##-- Test(True): https://python.org')
print(Bookmark.validate_url( 'https://python.org'))

print('##-- Test(False): http:://python.org')
print(Bookmark.validate_url(  'http:://python.org'))

print('##-- Test(False): http:/python.org')
print(Bookmark.validate_url(  'http:/python.org'))

print('##-- Test(False): https://python.org.42')
print(Bookmark.validate_url(  'https://python.org.42'))



# -------------------------------------------------------------------
print('\n\n' + '=' * 78)
print('Ex03: (✪✪✪) Create the ``BookmarkStash.valid_bookmarks`` property')

import urllib.request

class BookmarkStash:
    def __init__(self, name):
        self.name = name
        self.content = []

    def add(self, bookmark):
        if isinstance(bookmark, Bookmark) and bookmark.url not in self.content:
            self.content.append(bookmark)
        else:
            raise ValueError('Already there: {}'.format(bookmark.url))

    @classmethod
    def from_csv(cls, fname, name='Imported Bookmarkstash', delim=';'):
        try:
            # read file content
            bm_csv_l = open(fname, 'rt').readlines()
        except FileNotFoundError:
            print('Can not open {}'.format(fname))
            raise           # re-raise exception

        stash = cls(name)
        for rec in bm_csv_l[1:]:      # 1st line is header, skip!
            name, url = rec.strip().split(delim)
            bm = Bookmark(name, url)
            stash.add(bm)
        return stash

    @property
    def valid_bookmarks(self):
        valid_urls = []
        for bm in self.content:
            print('DEBUG: Trying: {}'.format(bm.url))
            try:
                conn = urllib.request.urlopen(bm.url)
            except urllib.error.URLError:
                print('DEBUG: Error opening: {}'.format(bm.url))
            else:
                valid_urls.append(bm)
        return valid_urls

    def __iter__(self):
        return iter(self.content)

    def __str__(self):
        return '{} ({})'.format(self.name, len(self.content))

    def __repr__(self):
        return '<BookmarkStash "{}">'.format(self.__str__())

    def __len__(self):
        return len(self.content)

    def __getitem__(self, what):
        if isinstance(what, (int, slice)):
            return self.content.__getitem__(what)
        elif isinstance(what, str):
            # required change for 2nd bullet Ex03---v
            return [ e for e in self.content if str(e).find(what) != -1  ]


# print('##-- Test: valid_bookmarks')
bm = BookmarkStash(name='Test: valid_bookmarks')
bm.add(Bookmark('Python Home', 'https://python.org'))
bm.add(Bookmark('Google Search', 'https://google.com'))
bm.add(Bookmark('LinkedIn', 'https://linkedin.com'))
bm.add(Bookmark('Phony URL', 'https://doesnotexists.com.sdfsdf'))
print(bm)
print(bm.valid_bookmarks)



