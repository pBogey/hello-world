"""
Decorators - Parametrization
23.08.2019
Bogdan Prădatu - Fluent Python
"""

registry = set()

def register(active=True): # decorator factory
    def decorate(func): # actual decorator
        print(f'running register (active = {active} -> decorate{func}')
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func # decorators return functions
    return decorate 

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')


if __name__ == "__main__":
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()
