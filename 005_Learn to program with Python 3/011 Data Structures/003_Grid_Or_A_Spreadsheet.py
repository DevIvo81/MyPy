import os
os.system('cls')

# Simple Tic Tac Toe grid

EMPTY = ' '
X = 'X'
Y = 'O'

# Build a 3 by 3 grid
grid =[\
        [EMPTY, EMPTY, EMPTY],\
        [EMPTY, EMPTY, EMPTY],\
        [EMPTY, EMPTY, EMPTY]\
        ]

# Typically set the row and col based on user input,
# this is just for demonstration
row = 0
col = 2
print(grid)
grid[row][col] = 'X'
print()
print(grid)
print()