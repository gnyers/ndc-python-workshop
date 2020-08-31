def fibonacci(n):               # doctest: +ELLIPSIS
    a, b = 0, 1
    i = 0
    while i < n:
        yield b
        a, b  = b, a+b
        i += 1

# Ex02
def factorial(n):
    # Recursive implementation, will cause problems if n ~ 1000
    # because of the built-in recursion limit in Python
    if n == 1: return 1
    else     : return n * factorial(n-1)

def factorial2(n):
    # This is a better implementation in Python, using a loop
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res

# Ex03
def season(month):
    seasons = {
        ('Dec', 'Jan', 'Feb'): 'winter',
        ('Mar', 'Apr', 'May'): 'spring',
        ('Jun', 'Jul', 'Aug'): 'summer',
        ('Sep', 'Oct', 'Nov'): 'fall'
    }
    for season in seasons:
        if month in season:
            return seasons[season]
    return f'Did not recognize {month}'

def season2(month):
    # This implementation is quicker but uses a bit more RAM
    seasons = {
            'Jan': 'winter',
            'Feb': 'winter',
            'Mar': 'spring',
            'Apr': 'spring',
            'May': 'spring',
            'Jun': 'summer',
            'Jul': 'summer',
            'Aug': 'summer',
            'Sep': 'fall',
            'Oct': 'fall',
            'Nov': 'fall',
    }
    return seasons.get(month, f'Did not recognize {month}')

# Ex04
def distance(*args):
    ret = []
    for e in args:
        # '16 mile' 
        dist, unit = e.split()
        try:
             dist = float(dist)
        except:
             pass
        if unit == 'mile':   dist_new = dist * 1.6
        elif unit == 'km':   dist_new = dist / 1.6
        ret.append(dist_new)
    return ret


# Ex05
vals = ['23.14', '33.3', '2.8', '13.1', '13.9', '3.4', '23.0', '32.9']
def sorter(numbers):
    return sorted(numbers, key=lambda nr: float(nr))


# Ex06
def avg(*args):
    ret = []
    for e in args:
        try:
            e = float(e)
            ret.append(e)
        except:
            pass
    return sum(ret) / len(ret)

# Ex07
def dedup(*args):
    elements = [ e.lower() for e in args ]
    deduped = set(elements)
    sorted_and_deduped = sorted(deduped)
    return tuple(sorted_and_deduped)


# Ex08
t = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
from collections import Counter
def counter(text):
    # The most beautiful implementation ;-)
    return dict(Counter(text.split()))

def counter2(text):
    # Less elegant but still nice
    ret = {}
    for word in text.split():
        nr_occurrances = ret.get(word, 0) + 1
        ret[word] = nr_occurrances
    return ret


# Ex09
t = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
'''
def analyze(text):
    # a bit densely packed implementation, but quite handy
    ret = {}
    for nr, line in enumerate(text.split('\n'), 1):
        for word in line.split():
            word = word.lower().strip('.,;-()"\'')
            ret.setdefault(word, []).append(nr)

    return ret



