"""
List comprehensions
16.07.2019
Bogdan Prădatu - Fluent Python
"""

symbols = "$¢£¥€¤"
codes = []
# generate list using loop
#for symb in symbol:
#    codes.append(ord(sym))
# generate list using list comprehensions
codes = [ord(sym) for sym in symbols]
print("codes:",codes)

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print("beyond_ascii:",beyond_ascii)

beyond_ascii = list(filter(lambda c: c >127, map(ord, symbols)))
print("beyond_ascii:",beyond_ascii)

# Create list o T-shirts available in two colors and three sizes
colors = ["black","white"]
sizes = ["S","M","L"]
tshirts = [(color,size) for color in colors
                        for size in sizes]
print("tshirts:",tshirts)

print("\n********** List Initialization **********")
board = [['_']*3 for i in range(3)]
print("board = [['_']*3 for i in range(3)]")
print("board:",board)
print("board[1][2] = 'X'")
board[1][2] = "X"
print("board:",board)
print()
weird_board = [['_']*3]*3
print("weird_board = [['_']*3]*3")
print("weird_board:",weird_board)
print("weird_board[1][2]='X'")
weird_board[1][2]='X'
print("weird_board:",weird_board)

# line breaks are ignored inside pairs of [], {}, or ().
print('\n')
abc = [x for x in range(2)
       for i in range(5)]
print("abc:", abc)
