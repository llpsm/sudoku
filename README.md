# Sudoku
Sudoku solver and generator written in Python.

## Usage
1. Clone Git Repository to local environment
git clone https://github.com/llpsm/sudoku.git

2. Modify the code

3. Save modifications on local repository (Commit changes)
git commit -m "<commit message>"

4. Save changes in remote repository
git push

### Code
```
from grid import Grid9x
from solver import Solve9x

grid_dict = {
	0: 5, 1: 0, 2: 3, 3: 6, 4: 0, 5: 0, 6: 7, 7: 2, 8: 0, 
	9: 0, 10: 0, 11: 8, 12: 0, 13: 2, 14: 0, 15: 5, 16: 0, 17: 1, 
	18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 5, 24: 0, 25: 0, 26: 0, 
	27: 2, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 9, 35: 0, 
	36: 0, 37: 3, 38: 0, 39: 0, 40: 9, 41: 0, 42: 0, 43: 4, 44: 0, 
	45: 0, 46: 1, 47: 0, 48: 0, 49: 0, 50: 0, 51: 0, 52: 0, 53: 5, 
	54: 0, 55: 0, 56: 0, 57: 1, 58: 0, 59: 0, 60: 0, 61: 0, 62: 0, 
	63: 1, 64: 0, 65: 5, 66: 0, 67: 7, 68: 0, 69: 6, 70: 0, 71: 0, 
	72: 0, 73: 8, 74: 7, 75: 0, 76: 0, 77: 6, 78: 2, 79: 0, 80: 4
}

grid = Grid9x(grid_dict)
Solve9x(grid)

print(grid.is_solved)
grid.print()
```
### Output
```
True

    5   9   3 | 6   1   4 | 7   2   8
    4   7   8 | 9   2   3 | 5   6   1
    6   2   1 | 7   8   5 | 4   3   9
    -   -   -   -   -   -   -   -   -
    2   5   4 | 8   3   7 | 1   9   6
    7   3   6 | 5   9   1 | 8   4   2
    8   1   9 | 4   6   2 | 3   7   5
    -   -   -   -   -   -   -   -   -
    3   6   2 | 1   4   8 | 9   5   7
    1   4   5 | 2   7   9 | 6   8   3
    9   8   7 | 3   5   6 | 2   1   4
```
