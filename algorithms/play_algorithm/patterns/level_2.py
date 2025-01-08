from algorithms.play_algorithm.validations.validations import Validations
from .deep_level import DeepLevel


class SecondLevel:
    def __init__(self, grid, r_void_cells, c_void_cells, m_grid_void_cells, possibleNumForCells):
        self.grid = grid
        self.r_void_cells = r_void_cells
        self.c_void_cells = c_void_cells
        self.m_grid_void_cells = m_grid_void_cells
        self.possibleNumForCells = possibleNumForCells
        self.k_strs = ["00", "03", "06", "30", "33", "36", "60", "63", "66"]
        self.validate = Validations(grid)

    def findSecondLevel(self):

        for i in range(9):
            if len(self.r_void_cells[i]) == 2:
                if self.fillValueForSecondLevel(self.r_void_cells[i], 'r'):
                    return True
            if len(self.c_void_cells[i]) == 2:
                if self.fillValueForSecondLevel(self.c_void_cells[i], 'c'):
                    return True
        for k_str in self.k_strs:
            if len(self.m_grid_void_cells[k_str]) == 2:
                cells = self.m_grid_void_cells[k_str]
                if self.fillValueForSecondLevel(cells, 'm_g'):
                    return True

        return False
    
    def fillValueForSecondLevel(self, cells, rowORcolORgrid):

        grid = self.grid
        if rowORcolORgrid == 'r':
            nums = []
            r = cells[0][0]
            for num in range(1, 10):
                if num not in grid[r]:
                    nums.append(num)
            return self.canFill(cells, nums)

        if rowORcolORgrid == 'c':
            nums = []
            c_nums = []
            col = cells[0][1]
            for ind in range(9):
                c_nums.append(self.grid[ind][col])
            for num in range(1, 10):
                if num not in c_nums:
                    nums.append(num)

            return self.canFill(cells, nums)

        if rowORcolORgrid == 'm_g':
            x, y = (cells[0][0] // 3) * 3, (cells[0][1] // 3) * 3
            m_g_nums = []
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    m_g_nums.append(grid[i][j])
            nums = []
            for num in range(1, 10):
                if num not in m_g_nums:
                    nums.append(num)
            return self.canFill(cells, nums)

    def canFill(self, cells, nums):
        grid = self.grid

        if self.isValid(cells[0], nums[0]) and not self.isValid(cells[1], nums[0]):
            r, c = cells[0][0], cells[0][1]
            num = nums[0]

        elif not self.isValid(cells[0], nums[0]) and self.isValid(cells[1], nums[0]):
            r, c = cells[1][0], cells[1][1]
            num = nums[0]

        elif self.isValid(cells[0], nums[1]) and not self.isValid(cells[1], nums[1]):
            r, c = cells[0][0], cells[0][1]
            num = nums[1]

        elif not self.isValid(cells[0], nums[1]) and self.isValid(cells[1], nums[1]):
            r, c = cells[1][0], cells[1][1]
            num = nums[1]
        else:
            # if cells[0][0] == cells[1][0]:
            #     rowORcol = "r"
            # else:
            #     rowORcol = "c"
            #
            # print("Deep Level Scan in level 2")
            # print(cells, nums, rowORcol)
            # deepLevel = DeepLevel(self.grid, self.r_void_cells, self.c_void_cells, self.m_grid_void_cells, self.possibleNumForCells)
            # for cell in cells:
            #     for num in nums:
            #         if rowORcol == "r":
            #             if deepLevel.deepScan(deepLevel.findAllRemGrids(cell[0], cell[1]), num):
            #                 print([cell[0] + 1, cell[1] + 1], " : ", num)
            #                 self.grid[cell[0]][cell[1]] = num
            #                 self.updateMissingCells(cell[0], cell[1])
            #                 self.updatePosValForCells(cell[0], cell[1], num)
            #                 print("Deep Second Level in Row")
            #
            #                 return True
            #             else:
            #                 if deepLevel.deepScan(deepLevel.findAllRemGrids(cell[0], cell[1]), num):
            #                     print([cell[0] + 1, cell[1] + 1], " : ", num)
            #                     self.grid[cell[0]][cell[1]] = num
            #                     self.updateMissingCells(cell[0], cell[1])
            #                     self.updatePosValForCells(cell[0], cell[1], num)
            #                     print("Deep Second Level in Col")
            #                     return True

            return False
        print([r + 1, c + 1], " : ", num)
        grid[r][c] = num
        self.updateMissingCells(r, c)
        self.updatePosValForCells(r, c, num)
        return True

    def isValid(self, cell, num):
        return self.validate.checkNumber(cell[0], cell[1], num)

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
            if cell == '06' and num == 8:
                print(cell)
            if cell[0] == str(r) and num in self.possibleNumForCells[cell]:
                self.possibleNumForCells[cell].remove(num)
            if cell[1] == str(c) and num in self.possibleNumForCells[cell]:
                self.possibleNumForCells[cell].remove(num)

    def fillValue(self, r, c, num):
        self.grid[r][c] = num
        pass