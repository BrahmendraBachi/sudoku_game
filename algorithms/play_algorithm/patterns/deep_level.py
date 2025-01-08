from .naked_pairs import NakedPairs
from algorithms.play_algorithm.validations.validations import Validations
from .level_1 import First_LeveL


class DeepLevel:

    def __init__(self, grid, r_void_cells, c_void_cells, m_grid_void_cells, possibleNumForCells):
        self.grid = grid
        self.r_void_cells = r_void_cells
        self.c_void_cells = c_void_cells
        self.m_grid_void_cells = m_grid_void_cells
        self.possibleNumForCells = possibleNumForCells
        self.k_strs = ["00", "03", "06", "30", "33", "36", "60", "63", "66"]
        self.validate = Validations(grid)
        self.nakedPairCheck = NakedPairs(self.possibleNumForCells)

    def checkDeepLevelForCol(self, cell_A, cell_B, num):

        r1, c1 = cell_A[0], cell_A[1]

        r2, c2 = cell_B[0], cell_B[1]

        c1_rem_grids = self.getRemainingGridsForRow(r1, c1)

        c2_rem_grids = self.getRemainingGridsForRow(r2, c2)

        if self.deepScan(c1_rem_grids, num) and not self.deepScan(c2_rem_grids, num):
            print([r1 + 1, c1 + 1], " : ", num)
            print("Deep Level Scan in Row")
            print()
            self.grid[r1][c1] = num
            self.updateMissingCells(r1, c1)
            self.updatePosValForCells(r1, c1, num)

            return True
        if self.deepScan(c2_rem_grids, num) and not self.deepScan(c1_rem_grids, num):
            print([r2 + 1, c2 + 1], " : ", num)
            print("Deep level Scan in Row")
            print()
            self.grid[r2][c2] = num
            self.updateMissingCells(r2, c2)
            self.updatePosValForCells(r2, c2, num)

            return True

    def getRemainingGridsForCol(self, r, c):
        x = (c // 3) * 3
        rem_grids = []
        for i in range(9):
            if i >= x and i < x + 3:
                continue
            if self.grid[r][i] == 0:
                rem_grids.append([r, i])
        return rem_grids

    def getRemainingGridsForRow(self, r, c):

        x = (r // 3) * 3
        rem_grids = []
        for i in range(9):
            if i >= x and i < x + 3:
                continue
            if self.grid[i][c] == 0:
                rem_grids.append([i, c])
        return rem_grids

    def deepScan(self, rem_grids, num):
        for grid in rem_grids:
            r, c = grid[0], grid[1]
            if self.validate.checkNumber(r, c, num):
                return False
        return True

    def checkDeepLevelForRow(self, cell_A, cell_B, num):

        r1, c1 = cell_A[0], cell_A[1]

        r2, c2 = cell_B[0], cell_B[1]

        r1_rem_grids = self.getRemainingGridsForCol(r1, c1)

        r2_rem_grids = self.getRemainingGridsForCol(r2, c2)

        if self.deepScan(r1_rem_grids, num) and not self.deepScan(r2_rem_grids, num):
            print([r1 + 1, c1 + 1], " : ", num)
            print("Deep Level Scan in Column")
            print()
            self.grid[r1][c1] = num
            self.updateMissingCells(r1, c1)
            self.updatePosValForCells(r1, c1, num)

            return True
        if self.deepScan(r2_rem_grids, num) and not self.deepScan(r1_rem_grids, num):
            print([r2 + 1, c2 + 1], " : ", num)
            print("Deep Level Scan in Column")
            self.grid[r2][c2] = num
            self.updateMissingCells(r2, c2)
            self.updatePosValForCells(r2, c2, num)

            return True

        return False

        pass

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

    def byPossibleValues(self):
        count = 0
        firstLevel = First_LeveL(self.grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells,
                                 self.possibleNumForCells)
        check = True
        while check:
            for i in range(9):
                for j in range(9):
                    cell = str(i) + str(j)
                    if cell in self.possibleNumForCells:
                        nums = self.possibleNumForCells[cell]
                        if len(nums) == 1:
                            num = nums[0]
                            self.grid[i][j] = num
                            print([i + 1, j + 1], " : ", num)
                            print("Possible values in 1 level")
                            print()
                            self.updateMissingCells(i, j)
                            self.updatePosValForCells(i, j, num)
                            count += 1
                            continue
                        # if len(nums) == 2:
                        #     if self.fillDeepInPossibleValues(cell, nums):
                        #         count += 1
                        #         continue

            check = False
            if count == 0:
                if self.nakedPairCheck.updatePossibleNumForCells():
                    print("NakedPairCheck is started")
                    return self.byPossibleValues()

        return count

    def fillDeepInPossibleValues(self, cell, nums):
        r, c = int(cell[0]), int(cell[1])
        num1, num2 = nums[0], nums[1]
        rem_grids = self.findAllRemGrids(r, c)
        if self.deepScan(rem_grids, num1) and not self.deepScan(rem_grids, num2):
            self.grid[r][c] = num1
            print([r + 1, c + 1], " : ", num1)
            print("Possible values in 2 level")
            print()
            self.updateMissingCells(r, c)
            self.updatePosValForCells(r, c, num1)
            return True
        if not self.deepScan(rem_grids, num1) and self.deepScan(rem_grids, num2):
            self.grid[r + 1][c + 1] = num2
            print([r, c], " : ", num2)
            print("Possible values in 2 level")
            print()
            self.updateMissingCells(r, c)
            self.updatePosValForCells(r, c, num2)
            return True

        return False

    def findAllRemGrids(self, r, c):
        rem_grids = []
        for i in range(9):
            if self.grid[r][i] == 0 and i != c:
                rem_grids.append([r, i])
            if self.grid[i][c] == 0 and i != r:
                rem_grids.append([i, c])

        return rem_grids


