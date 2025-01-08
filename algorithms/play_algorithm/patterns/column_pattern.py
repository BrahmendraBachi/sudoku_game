from algorithms.play_algorithm.validations.validations import Validations
from .deep_level import DeepLevel

class ColumnPattern:

    def __init__(self, grid, r_void_cells, c_void_cells, m_grid_void_cells, possibleNumForCells):
        self.grid = grid
        self.r_void_cells = r_void_cells
        self.c_void_cells = c_void_cells
        self.m_grid_void_cells = m_grid_void_cells
        self.possibleNumForCells = possibleNumForCells
        self.k_strs = ["00", "03", "06", "30", "33", "36", "60", "63", "66"]
        self.validate = Validations(grid)
        self.filledCount = 0

    def fillGridColumns(self):
        grid = self.grid
        for i in range(0, 3):
            c_a, c_b, c_c = (i * 3), (i * 3) + 1, (i * 3) + 2
            pairs = [[c_a, c_b], [c_a, c_c], [c_b, c_c]]
            for pair in pairs:
                c1, c2 = pair[0], pair[1]
                
                c1_Nums = self.getNumbersForColInd(c1)
                c2_Nums = self.getNumbersForColInd(c2)
                
                set1 = set(c1_Nums)
                set2 = set(c2_Nums)
                
                commonNums = set1.intersection(set2)

                ind_c = (c_a + c_b + c_c - (c1 + c2))
                
                ind_c_Nums = self.getNumbersForColInd(ind_c)

                for num in commonNums:

                    if num in ind_c_Nums or num == 0:
                        continue

                    r1 = c1_Nums.index(num)
                    r2 = c2_Nums.index(num)
                    

                    r1 = r1 // 3
                    r2 = r2 // 3

                    rem_r = (3 - (r1 + r2)) * 3

                    if self.tryFill(rem_r, ind_c, num) == "deep":
                        self.filledCount += 1
        return self.filledCount
    
    def tryFill(self, rem_r, ind_c, num):
        grid = self.grid

        isValid = False
        cell_A, cell_B, cell_C = [rem_r, ind_c], [rem_r + 1, ind_c], [rem_r + 2, ind_c]
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
                if deepLevel.checkDeepLevelForRow(cell_B, cell_C, num):
                    return "deep"
            elif not self.validate.checkNumber(cell_B[0], cell_B[1], num):
                if deepLevel.checkDeepLevelForRow(cell_A, cell_C, num):
                    return "deep"
            elif not self.validate.checkNumber(cell_C[0], cell_C[1], num):
                if deepLevel.checkDeepLevelForRow(cell_A, cell_B, num):
                    return "deep"
            else:
                for cell in [cell_A, cell_B, cell_C]:
                    if deepLevel.deepScan(deepLevel.getRemainingGridsForCol(cell[0], cell[1]), num):
                        print(cell, " : ", num)
                        self.grid[cell[0]][cell[1]] = num
                        self.updateMissingCells(cell[0], cell[1])
                        self.updatePosValForCells(cell[0], cell[1], num)

                        print("Deep Third Level in Col")
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
    
    def getNumbersForColInd(self, col):
        return [self.grid[i][col] for i in range(9)]

    def updatePosValForCells(self, r, c, num):
        key = str(r) + str(c)
        del self.possibleNumForCells[key]
        for cell in self.possibleNumForCells:
            if cell[0] == str(r) and num in self.possibleNumForCells[cell]:
                self.possibleNumForCells[cell].remove(num)
            if cell[1] == str(c) and num in self.possibleNumForCells[cell]:
                self.possibleNumForCells[cell].remove(num)

