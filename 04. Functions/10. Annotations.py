"""
Function annotations
14.08.2019
Bogdan Prădatu - Fluent Python
"""

from inspect import signature


# eac argument in the function declaration may have an annotation
# expression preceded by :. If there is a default value, the annotation
# goes between the argument name and the = sign.
# To annotate the return value, add -> and another expression between the )
# and the : at the tail of the function declaration.
# Annotations are not processed, but merely stored in the __annotations__ attr.
# No checks, enforcement, validation or any other action is performed.
def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """
    Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()


sig = signature(clip)
print("clip.__annotations__:", clip.__annotations__)
print("sig.return_annotation:", sig.return_annotation)
for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)
