from algorithms.play_algorithm.validations.validations import Validations

class Fourth_Level:

    def __init__(self, grid, r_void_cells, c_void_cells, m_grid_void_cells, possibleNumForCells):
        self.grid = grid
        self.r_void_cells = r_void_cells
        self.c_void_cells = c_void_cells
        self.m_grid_void_cells = m_grid_void_cells
        self.possibleNumForCells = possibleNumForCells
        self.k_strs = ["00", "03", "06", "30", "33", "36", "60", "63", "66"]
        self.validate = Validations(grid)

    def findFourthLevel(self):

        for i in range(9):
            if len(self.r_void_cells[i]) == 4:
                if self.fillValueForFourthLevel(self.r_void_cells[i], 'r'):
                    return True
            if len(self.c_void_cells[i]) == 4:
                if self.fillValueForFourthLevel(self.c_void_cells[i], 'c'):
                    return True
        for k_str in self.k_strs:
            if len(self.m_grid_void_cells[k_str]) == 4:
                if self.fillValueForFourthLevel(self.m_grid_void_cells[k_str], 'm_g'):
                    return True
        return False

    def fillValueForFourthLevel(self, cells, rowORcolORgrid):
        grid = self.grid
        nums = []
        if rowORcolORgrid == 'r':
            r = cells[0][0]
            for num in range(1, 10):
                if num not in grid[r]:
                    nums.append(num)
            return self.canFill(cells, nums)

        if rowORcolORgrid == 'c':
            c = cells[0][1]
            nums_p = []
            for i in range(9):
                nums_p.append(grid[i][c])
            for num in range(1, 10):
                if num not in nums_p:
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
        isValid = False
        cell_A, cell_B, cell_C, cell_D = cells[0], cells[1], cells[2], cells[3]

        for num in nums:

            if self.checkNumberForOneCell(cell_A, cell_B, cell_C, cell_D, num):
                r, c = cell_A[0], cell_A[1]
                isValid = True
                break

            if self.checkNumberForOneCell(cell_B, cell_A, cell_C, cell_D, num):
                r, c = cell_B[0], cell_B[1]
                isValid = True
                break

            if self.checkNumberForOneCell(cell_C, cell_A, cell_B, cell_D, num):
                r, c = cell_C[0], cell_C[1]
                isValid = True
                break

            if self.checkNumberForOneCell(cell_D, cell_A, cell_B, cell_C, num):
                r, c = cell_D[0], cell_D[1]
                isValid = True
                break

        if isValid:
            print([r + 1, c + 1], " : ", num)
            grid[r][c] = num
            self.updateMissingCells(r, c)
            self.updatePosValForCells(r, c, num)
            return True
        return False

    def checkNumberForOneCell(self, cell_A, cell_B, cell_C, cell_D, num):
        return self.validate.checkNumber(cell_A[0], cell_A[1], num) \
            and not self.validate.checkNumber(cell_B[0], cell_B[1], num) \
            and not self.validate.checkNumber(cell_C[0], cell_C[1], num) \
            and not self.validate.checkNumber(cell_D[0], cell_D[1], num)

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

