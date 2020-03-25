"""
Decorators - Clock Deco
23.08.2019
Bogdan Prădatu - Fluent Python
"""

import time
import functools

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter()
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' %(elapsed, name, arg_str, result))
        return result
    return clocked

def clock2(func):
    @functools.wraps(func) # functools.wraps copies the relevant attirbutes from func to clocked
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k,w) for k,w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' %(elapsed, name, arg_str, result))
        return result
    return clocked
