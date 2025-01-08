class First_LeveL:

    def __init__(self, grid, r_void_cells, c_void_cells, m_grid_void_cells, possibleNumForCells):
        self.grid = grid
        self.r_void_cells = r_void_cells
        self.c_void_cells = c_void_cells
        self.m_grid_void_cells = m_grid_void_cells
        self.possibleNumForCells = possibleNumForCells
        self.k_strs = ["00", "03", "06", "30", "33", "36", "60", "63", "66"]

    def findFirstLevel(self):

        for i in range(9):

            if len(self.r_void_cells[i]) == 1:
                self.fillValueForFirstLevel(self.r_void_cells[i][0], 'r')
                self.updateMissingCellsForFirstLevel(self.r_void_cells[i][0])
                return True

            if len(self.c_void_cells[i]) == 1:
                self.fillValueForFirstLevel(self.c_void_cells[i][0], 'c')
                self.updateMissingCellsForFirstLevel(self.c_void_cells[i][0])
                return True

        for k_str in self.k_strs:
            if len(self.m_grid_void_cells[k_str]) == 1:
                cell = self.m_grid_void_cells[k_str][0]
                self.fillValueForFirstLevel(cell, 'm_g')
                self.updateMissingCellsForFirstLevel(cell)
                return True
        return False

    def fillValueForFirstLevel(self, cell, rowORcolORgrid):
        r, c = cell[0], cell[1]
        grid = self.grid
        if rowORcolORgrid == 'r':
            for num in range(1, 10):
                if num not in grid[r]:
                    grid[r][c] = num
                    print([r + 1, c + 1], " : ", num)
                    self.updatePosValForCells(r, c, num)
                    break
        elif rowORcolORgrid == 'c':
            colNums = [grid[i][c] for i in range(9)]
            for num in range(1, 10):
                if num not in colNums:
                    grid[r][c] = num
                    print([r + 1, c + 1], " : ", num)
                    self.updatePosValForCells(r, c, num)
                    break
        else:
            x, y = ((r // 3) * 3), ((c // 3) * 3)
            m_g_nums = []
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    m_g_nums.append(grid[i][j])
            for num in range(1, 10):
                if num not in m_g_nums:
                    print([r + 1, c + 1], " : ", num)
                    self.updatePosValForCells(r, c, num)
                    grid[r][c] = num
                    break

    def updateMissingCellsForFirstLevel(self, cell):

        r, c = cell[0], cell[1]
        self.r_void_cells[r].remove(cell)
        self.c_void_cells[c].remove(cell)
        x, y = ((r // 3) * 3, (c // 3) * 3)
        k_str = str(x) + str(y)
        self.m_grid_void_cells[k_str].remove(cell)

    def updatePosValForCells(self, r, c, num):
        key = str(r) + str(c)
        del self.possibleNumForCells[key]

        for cell in self.possibleNumForCells:
            if cell[0] == str(r) and num in self.possibleNumForCells[cell]:
                self.possibleNumForCells[cell].remove(num)
            if cell[1] == str(c) and num in self.possibleNumForCells[cell]:
                self.possibleNumForCells[cell].remove(num)
