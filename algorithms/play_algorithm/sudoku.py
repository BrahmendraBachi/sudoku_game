# from algorithms.play_algorithm.patterns import column_pattern, row_pattern
from .patterns import row_pattern, column_pattern
# from algorithms.play_algorithm.patterns.level_1 import First_LeveL
from .patterns.level_1 import First_LeveL
from .patterns.level_2 import SecondLevel
from .patterns.level_3 import Third_Level
from .patterns.level_4 import Fourth_Level
# from algorithms.play_algorithm.patterns.level_2 import SecondLevel
# from algorithms.play_algorithm.patterns.level_3 import Third_Level
# from algorithms.play_algorithm.patterns.level_4 import Fourth_Level
# from validations.validations import Validations
from .validations.validations import  Validations
from .patterns.deep_level import DeepLevel
from .patterns.eliminate_cells_in_grid import EliminateCellsInGrid


class Sudoku:

    def __init__(self, grid):
        self.grid = grid
        self.numLocations = {}
        self.r_void_cells = {}
        self.c_void_cells = {}
        self.k_strs = ["00", "03", "06", "30", "33", "36", "60", "63", "66"]
        self.m_grid_void_cells = {"00": [], "03": [], "06": [],
                                  "30": [], "33": [], "36": [],
                                  "60": [], "63": [], "66": []}
        self.check = True
        self.basic = True

        for i in range(0, 9):
            self.r_void_cells[i] = []
            self.c_void_cells[i] = []
            self.numLocations[i + 1] = []

        self.numNotPresent = [self.r_void_cells, self.c_void_cells]


        self.missingNumbers = 0
        self.findMissedNumbers()

        self.possibleNumForCells = {}

        self.validate = Validations(self.grid)
        self.deepLevel = DeepLevel(self.grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells,
                                   self.possibleNumForCells)

        self.findPossibleNumForCells()

        self.byEliminate = EliminateCellsInGrid(self.grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells, self.possibleNumForCells)



        print(self.r_void_cells)
        print(self.c_void_cells)
        print(self.m_grid_void_cells)
        print(self.missingNumbers)
        print(self.possibleNumForCells)

        pass

    def findPossibleNumForCells(self):
        for i in range(9):
            for j in range(9):
                posNums = []
                if self.grid[i][j] == 0:
                    for num in range(1, 10):
                        if self.validate.checkNumber(i, j, num):
                            posNums.append(num)
                else:
                    continue
                self.possibleNumForCells[str(i) + str(j)] = posNums
        pass

    def findMissedNumbers(self):
        self.missingNumbers = 0
        grid = self.grid
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    self.missingNumbers += 1
                    self.r_void_cells[i].append([i, j])
                    self.c_void_cells[j].append([i, j])
                    k_str = str((i // 3) * 3) + str((j // 3) * 3)
                    self.m_grid_void_cells[k_str].append([i, j])
        pass

    def startGame(self):
        self.check = True
        while self.check and self.missingNumbers:
            if self.findRowPatters():
                self.check = True
                continue

            if self.findColumnPatterns():
                self.check = True
                continue

            if self.findBasicPatterns():
                self.check = True
                continue

            if self.fillByEliminatingCellsInGrid():
                self.check = True
                continue

            if self.findByPossibleValues():
                self.check = True
                continue

            self.check = False
        if self.missingNumbers == 0:
            print("Filling sudoku completed successfully")

        else:
            print("Code got stuck")

    def findBasicPatterns(self):
        isFilled = False
        self.basic = True
        print("Checking Basic Patterns has started")
        firstLevel = First_LeveL(self.grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells,
                                 self.possibleNumForCells)
        secondLevel = SecondLevel(self.grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells,
                                  self.possibleNumForCells)
        thirdLevel = Third_Level(self.grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells,
                                 self.possibleNumForCells)
        fourthLevel = Fourth_Level(self.grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells,
                                   self.possibleNumForCells)

        while self.basic and self.missingNumbers:
            if firstLevel.findFirstLevel():
                isFilled = True
                self.missingNumbers -= 1
                print("First Level")
                print()
                continue
            if secondLevel.findSecondLevel():
                isFilled = True
                self.missingNumbers -= 1
                print("Second Level")
                print()
                continue
            if thirdLevel.findThirdLevel():
                isFilled = True
                self.missingNumbers -= 1
                print("Third Level")
                print()
                continue

            if fourthLevel.findFourthLevel():
                isFilled = True
                self.missingNumbers -= 1
                print("Fourth Level")
                print()
                continue
            self.basic = False

        print("Updated Missing number count is: ", self.missingNumbers)
        # print("Updated grid is : ")
        # self.printGrid()
        # print()
        return isFilled

    def findColumnPatterns(self):
        grid = self.grid
        print("Column Patterns has started")
        columnPatterns = column_pattern.ColumnPattern(grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells,
                                                      self.possibleNumForCells)
        count = columnPatterns.fillGridColumns();
        self.missingNumbers -= count
        print("Updated via Column Pattern Number count is : ", count)
        print("Updated Missing number count is: ", self.missingNumbers)
        # print("Updated grid : ")
        # print(self.printGrid())
        # print()
        return count

    def findRowPatters(self):
        grid = self.grid
        print("Checking Row Patterns has started")
        rowPatterns = row_pattern.RowPattern(grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells,
                                             self.possibleNumForCells)
        count = rowPatterns.fillGridRows()
        self.missingNumbers -= count
        print("Updated via Row Patten number count is : ", count)
        print("Updated Missing number count is: ", self.missingNumbers)
        # print("Updated grid is : ")
        # self.printGrid()
        # print()
        return count

    def fillByEliminatingCellsInGrid(self):
        print("FillByEliminatingCellsInGrid has started")
        count = self.byEliminate.checkPossibleNumToEliminate()
        self.missingNumbers -= count
        print("Updated count via FillByEliminatingCellsInGrid : ", count)
        print("Updated Missing number count is: ", self.missingNumbers)
        # print("Updated grid is : ")
        # self.printGrid()
        # print()
        return count





    def findByPossibleValues(self):
        print("Checking By Possible Values for Grid has started")
        count = self.deepLevel.byPossibleValues()
        self.missingNumbers -= count
        print("Updated via checking by Possible values for Grid: ", self.missingNumbers)
        print("Updated Missing number count is: ", self.missingNumbers)

        return count

    def printGrid(self):

        grid = self.grid
        for row in grid:
            for num in row:
                print(num, end=" ")
            print()
