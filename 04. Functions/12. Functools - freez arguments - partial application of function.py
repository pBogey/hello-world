"""
Functools
14.08.2019
Bogdan Prădatu - Fluent Python
"""

from operator import mul
from functools import partial

# functools.partial is a higher-order function that allows partial application
# of a function. Given a function, a partial application produces a new callable
# with some of the arguments of the original function fixed.

## functools.partialmethod function does the same job as partial,
## but is designed to work with methods.

triple = partial(mul, 3)

print("triple(7):",triple(7))

print(list(map(triple, range(1,10))))

import unicodedata

nfc = partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'

print("s1:",s1,"\ns2:",s2)
print("s1 == s2:",s1==s2)
print("nfc(s1)==nfc(s2):",nfc(s1)==nfc(s2))

print("\n***********          ***********\n")

def tag(name, *content, cls=None, **attrs):
    """ Generate one or more HTML tags """
    # test_variable has no use, it's just for exemplification
    test_variable = None
    
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('h1', 'Chapter 1', cls='title', color='red'))

picture = partial(tag, 'img', cls='pic-frame')
print(tag(name='img', cls='pic-frame', src='wumpus.jpeg'))
print(picture(src='wumpus.jpeg'))