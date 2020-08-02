"""
Sorting
08.08.2019
Bogdan Prădatu
"""

import pyuca  # PyUCA - Unicode Collation Algorithm (UCA)


coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits)
sorted_fruits_UCA = sorted(fruits, key=coll.sort_key)
print("furits:", "\t\t", fruits)
print("sorted_furits:", "\t\t", sorted_fruits)
print("sorted_furits_UCA:", "\t", sorted_fruits_UCA)
