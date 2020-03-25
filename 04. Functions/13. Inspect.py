"""
Inspect
21.08.2019
Bogdan Prădatu - Fluent Python
"""

import Fruitful_functions
import inspect

for func in inspect.getmembers(Fruitful_functions, inspect.isfunction):
    print(func)
