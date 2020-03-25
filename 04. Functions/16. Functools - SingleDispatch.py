"""
Functools - singledispatch
23.08.2019
Bogdan Prădatu - Fluent Python
"""

## PEP 443 -- Single-dispatch generic functions
## https://www.python.org/dev/peps/pep-0443/

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch # marks the base function that handles the object type
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'

@htmlize.register(str) # each specialized function is decorated with
                       # @<<base function>>.register(<<type>>)
def _(text):           # the name of the specialized function is irrelevant
    content = html.escape(text).replace('\n','<br>/n')
    return f'<p>{content}</p>'

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)                # Stack multiple registers decorators
@htmlize.register(abc.MutableSequence)  # to support different types with same func
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n</li>' + inner + '</li>\n</ul>'


if __name__ == "__main__":
    print(htmlize({1,2,3}))
    print(htmlize(abs))
    print(htmlize('Heimlich & Co.\n- a game'))
    print(htmlize(42))
    print(htmlize(['alpha', 66, {3, 2, 1}]))
