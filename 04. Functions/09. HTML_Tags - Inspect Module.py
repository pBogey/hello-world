"""
Generate HTML tags
14.08.2019
Bogdan Prădatu - from Fluent Python
"""

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

print(tag('br'))
# any number of arguments after the first are captured by *content as a tuple
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
# keyword arguments not explicitly named in the tag signature are captured by
# **attrs as a dictionary
print(tag('p', 'hello', id=33))
# the cls parameter can only be passed as a keyword argument
print(tag('p', 'hello', 'world', cls='sidebar'))

my_tag = {'name':'img', 'title':'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls':'framed'}
# prefixing my_tag dict with ** passes all its items as separate arguments,
# which are then bound to the named parameters, with the remaining caught by
# **attrs
print(tag(**my_tag))

print("\ntag.__code__:",tag.__code__)
# the function arguments appear in co_varnames, but this also includes
# the local variables defined in the function body (test_variable)
print("tag.__code__.co_varnames:",tag.__code__.co_varnames)
# the argument names are the first N strings, where N is given by co_argcount.
# This does not include the arguments prefixed with * or **, though
print("tag.__code__.co_argcount:",tag.__code__.co_argcount)
print("tag.__kwdefaults__:",tag.__kwdefaults__)

print("\n********** Inspect module **********")
from inspect import signature
sig = signature(tag)
print("signature(tag):",sig)
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

## binding the function signature from the tag function to a dict of args
bound_args = sig.bind(**my_tag)
print("\nbound_args:",bound_args)
for name, value in bound_args.arguments.items():
    print(name, '=', value)

## remove mandatory argument 'name'. Calling sig.bind(**my_tag) raises
## TypeError complaining of the missing name parameter
#del my_tag['name']
#bound_args = sig.bind(**my_tag)

## keyword only arguments
print("\n***** Keyword only arguments      *****")
# to specify keyword only arguments when naming a function,
# name them after the argument prefixed with *.
def f(a,*,b):
    return a,b

print(f(1, b=2))
