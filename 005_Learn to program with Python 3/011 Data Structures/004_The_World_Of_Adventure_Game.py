# 004_The_World_Of_Adventure_Game

import os
os.system('cls')

# Adventure game demo dynamic

import random

EMPTY = 'E'
TREASURE = 'T'
MONSTER = 'M'
SWORD = 'S'
POTION= 'P'
addInToGrid = (TREASURE, TREASURE, TREASURE, MONSTER, MONSTER, MONSTER,\
                SWORD, SWORD, POTION, POTION)


N_ROWS_IN_GRID = 6
N_COLS_IN_GRID = 8

# build 6 by 6 grid

# Find a random cell that is empty
def findEmptyCell(aGrid, nRows, nCols):
    while True:
        aRow = random.randrange(nRows)
        aCol = random.randrange(nCols)
        if aGrid[aRow][aCol] == EMPTY:
            return aRow, aCol

# Build grid, start it off all empty
grid = []
# Build one row, start it off all empty
for r in range(N_ROWS_IN_GRID):
    aRow = []
    for c in range(N_COLS_IN_GRID):
        aRow.append(EMPTY)
    grid.append(aRow)

# Add items randomly
for item in addInToGrid:
    locRow, locCol = findEmptyCell(grid, N_ROWS_IN_GRID, N_COLS_IN_GRID)
    grid[locRow][locCol] = item

# For testing, print the grid, row by row
for thisRow in grid:
    print(thisRow)
print()
locRow, locCol = findEmptyCell(grid, N_ROWS_IN_GRID, N_COLS_IN_GRID)

# For testing, print out the starting location so we know
# where we are in the grid
print(f'\nStarting at row:{locRow}, col:{locCol}')

# Move around the grid

while True:
    direction = input('\nPress L, U, R or D to move: ').lower()
    
    if direction == 'l':
        locCol -= 1
    elif direction == 'u':
        locRow -= 1
    elif direction == 'r':
        locCol += 1
    elif direction == 'd':
        locRow += 1
    else:
        print('\nGoing nowhere...')

    foundInCell = grid[locRow][locCol]
    print(f'Now at row: {locRow}, col:{locCol},     cell contains:{foundInCell}')
