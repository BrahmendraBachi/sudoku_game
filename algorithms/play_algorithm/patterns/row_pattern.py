from algorithms.play_algorithm.validations.validations import Validations
from .deep_level import DeepLevel
# import sudoku

class RowPattern:

    def __init__(self, grid, r_void_cells, c_void_cells, m_grid_void_cells, possibleNumForCells):
        self.grid = grid
        self.r_void_cells = r_void_cells
        self.c_void_cells = c_void_cells
        self.m_grid_void_cells = m_grid_void_cells
        self.possibleNumForCells = possibleNumForCells
        self.k_strs = ["00", "03", "06", "30", "33", "36", "60", "63", "66"]
        self.validate = Validations(grid)
        self.filledCount = 0

    def fillGridRows(self):

        grid = self.grid
        
        for i in range(3):
            r_a, r_b, r_c = (i * 3), (i * 3) + 1, (i * 3) + 2
            pairs = [[r_a, r_b], [r_a, r_c], [r_b, r_c]]
            for pair in pairs:
                r1, r2 = pair[0], pair[1]
                set1 = set(grid[r1])
                set2 = set(grid[r2])
                commonNums = list(set1.intersection(set2))

                ind_r = (r_a + r_b + r_c - (r1 + r2))
                for num in commonNums:
                    if num in grid[ind_r] or num == 0:
                        continue
                    c1 = grid[r1].index(num)
                    c2 = grid[r2].index(num)

                    c1 = (c1 // 3)
                    c2 = (c2 // 3)

                    rem_c = (3 - (c1 + c2)) * 3
                    if self.tryFill(ind_r, rem_c, num) == "deep":
                        self.filledCount += 1
        return self.filledCount

    def tryFill(self, ind_r, rem_c, num):

        grid = self.grid

        isValid = False
        cell_A, cell_B, cell_C = [ind_r, rem_c], [ind_r, rem_c + 1], [ind_r, rem_c + 2]
        if self.checkValid(cell_A, cell_B, cell_C, num):
            r, c = cell_A[0], cell_A[1]
            isValid = True

        elif self.checkValid(cell_B, cell_A, cell_C, num):
            r, c = cell_B[0], cell_B[1]
            isValid = True

        elif self.checkValid(cell_C, cell_A, cell_B, num):
            r, c = cell_C[0], cell_C[1]
            isValid = True

        else:
            deepLevel = DeepLevel(self.grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells, self.possibleNumForCells)
            if not self.validate.checkNumber(cell_A[0], cell_A[1], num):
                if deepLevel.checkDeepLevelForCol(cell_B, cell_C, num):
                    return "deep"
            elif not self.validate.checkNumber(cell_B[0], cell_B[1], num):
                if deepLevel.checkDeepLevelForCol(cell_A, cell_C, num):
                    return "deep"
            elif not self.validate.checkNumber(cell_C[0], cell_C[1], num):
                if deepLevel.checkDeepLevelForCol(cell_A, cell_B, num):
                    return "deep"
            else:
                for cell in [cell_A, cell_B, cell_C]:
                    if deepLevel.deepScan(deepLevel.getRemainingGridsForRow(cell[0], cell[1]), num):
                        print(cell, " : ", num)
                        self.grid[cell[0]][cell[1]] = num
                        self.updateMissingCells(cell[0], cell[1])
                        self.updatePosValForCells(cell[0], cell[1], num)
                        print("Deep Third Level in Row")
                        print()
                        return "deep"

            return isValid
        print([r + 1, c + 1], " : ", num)
        print()
        self.filledCount += 1
        grid[r][c] = num

        self.updateMissingCells(r, c)
        self.updatePosValForCells(r, c, num)

        return isValid



    def checkValid(self, cell_A, cell_B, cell_C, num):
        return self.validate.checkNumber(cell_A[0], cell_A[1], num) \
            and not self.validate.checkNumber(cell_B[0], cell_B[1], num) \
            and not self.validate.checkNumber(cell_C[0], cell_C[1], num)

    def updateMissingCells(self, r, c):

        self.r_void_cells[r].remove([r, c])
        self.c_void_cells[c].remove([r, c])
        k_str = str((r // 3) * 3) + str((c // 3) * 3)
        self.m_grid_void_cells[k_str].remove([r, c])

        pass

    def updatePosValForCells(self, r, c, num):
        key = str(r) + str(c)
        del self.possibleNumForCells[key]
        for cell in self.possibleNumForCells:
            if cell[0] == str(r) and num in self.possibleNumForCells[cell]:
                self.possibleNumForCells[cell].remove(num)
            if cell[1] == str(c) and num in self.possibleNumForCells[cell]:
                self.possibleNumForCells[cell].remove(num)


