import time

from algorithms.play_algorithm.sudoku import Sudoku
from sudokuGrids.easy import easyGrids

if __name__ == '__main__':
    st = time.time()
    # grid = hardGrids.grid5
    # grid = mediumGrids.grid2
    grid = easyGrids.grid2
    # grid = expertGrids.grid1

    game = Sudoku(grid)
    game.startGame()
    print(game.missingNumbers)
    game.printGrid()

    # game.findPossibleNumForCells()
    # game.findByPossibleValues()
    # print(game.possibleNumForCells)
    # print(game.printGrid())

    # print(game.r_void_cells)
    # print(game.c_void_cells)
    # print(game.m_grid_void_cells)
    # print(game.possibleNumForCells)

    en = time.time()
    print(en - st)

    # sudokuBacktracking.giveSuduko(game.grid)
    # game.printGrid()

    en = time.time()
    print(en - st)