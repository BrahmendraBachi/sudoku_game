class EliminateCellsInGrid:

    def __init__(self, grid, r_void_cells, c_void_cells, m_grid_void_cells, possibleNumForCells):
        self.grid = grid
        self.r_void_cells = r_void_cells
        self.c_void_cells = c_void_cells
        self.m_grid_void_cells = m_grid_void_cells
        self.possibleNumForCells = possibleNumForCells
        self.k_strs = ["00", "03", "06", "30", "33", "36", "60", "63", "66"]

    def checkPossibleNumToEliminate(self):
        count = 0
        for i in range(9):
            for j in range(9):
                cell = self.getRemCellsInGrids(i, j)
                if not cell:
                    continue
                r, c = cell[0], cell[1]
                num = self.commonNumInRemRowsAndCols(i, j)
                if num:
                    self.fillNum(r, c, num)
                    print([r + 1, c + 1], " : ", num)
                    print("By Eliminating Rows and Cols")
                    print()
                    count += 1
        return count



    def getRemCellsInGrids(self, r, c):
        cell = []
        x = (r // 3) * 3
        y = (c // 3) * 3
        isDone = False
        for i in range(x, x + 3):
            if i == r:
                continue
            for j in range(y, y + 3):
                if j == c:
                    continue
                if self.grid[i][j] == 0:
                    if not isDone:
                        cell = [i, j]
                        isDone = True
                    else:
                        isDone = False
                        break
            if not isDone:
                break
        if isDone:
            return cell
        else:
            return []

    def commonNumInRemRowsAndCols(self, r, c):
        rem_row_nums = self.getRowNums(r, c)
        rem_col_nums = self.getColNums(r, c)

        commonNums = list(set(rem_row_nums).intersection(set(rem_col_nums)))

        validNum = 0


        for num in commonNums:
            if not self.isPresentInGrid(r, c, num):
                validNum = num
                break

        if validNum:
            return validNum
        else:
            return 0

    def getRowNums(self, r, c):
        x = (c // 3) * 3
        rem_nums = []
        for i in range(9):
            if i >= x and i < x + 3:
                continue
            if self.grid[r][i] != 0:
                rem_nums.append(self.grid[r][i])
        return rem_nums

    def getColNums(self, r, c):
        x = (r // 3) * 3
        rem_nums = []
        for i in range(9):
            if i >= x and i < x + 3:
                continue
            if self.grid[i][c] != 0:
                rem_nums.append(self.grid[i][c])
        return rem_nums

    def fillNum(self, r, c, num):

        self.grid[r][c] = num
        self.updateMissingCells(r, c)
        self.updatePosValForCells(r, c, num)

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

    def isPresentInGrid(self, r, c, num):

        x = (r // 3) * 3
        y = (c // 3) * 3
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if num == self.grid[i][j]:
                    return True
        return False


if __name__ == '__main__':
    grid = [[0, 7, 0, 0, 0, 0, 0, 0, 8], [0, 5, 0, 0, 4, 0, 0, 2, 7], [9, 0, 0, 0, 7, 1, 5, 0, 0], [6, 0, 5, 1, 3, 0, 9, 7, 4],
     [7, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 7, 6, 0, 0, 0, 5], [1, 9, 7, 0, 0, 3, 0, 0, 2], [0, 4, 0, 0, 1, 0, 7, 0, 0],
     [5, 0, 8, 4, 2, 7, 0, 0, 0]]

    r_void_cells = {0: [[0, 0], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]], 1: [[1, 0], [1, 2], [1, 3], [1, 5], [1, 6]],
     2: [[2, 1], [2, 2], [2, 3], [2, 7], [2, 8]], 3: [[3, 1], [3, 5]],
     4: [[4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 7], [4, 8]], 5: [[5, 0], [5, 1], [5, 2], [5, 5], [5, 6], [5, 7]],
     6: [[6, 3], [6, 4], [6, 6], [6, 7]], 7: [[7, 0], [7, 2], [7, 3], [7, 5], [7, 7], [7, 8]],
     8: [[8, 1], [8, 6], [8, 7], [8, 8]]}

    c_void_cells = {0: [[0, 0], [1, 0], [5, 0], [7, 0]], 1: [[2, 1], [3, 1], [4, 1], [5, 1], [8, 1]],
     2: [[0, 2], [1, 2], [2, 2], [4, 2], [5, 2], [7, 2]], 3: [[0, 3], [1, 3], [2, 3], [4, 3], [6, 3], [7, 3]],
     4: [[0, 4], [4, 4], [6, 4]], 5: [[0, 5], [1, 5], [3, 5], [4, 5], [5, 5], [7, 5]],
     6: [[0, 6], [1, 6], [5, 6], [6, 6], [8, 6]], 7: [[0, 7], [2, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7]],
     8: [[2, 8], [4, 8], [7, 8], [8, 8]]}

    m_grid_void_cells = {'00': [[0, 0], [0, 2], [1, 0], [1, 2], [2, 1], [2, 2]], '03': [[0, 3], [0, 4], [0, 5], [1, 3], [1, 5], [2, 3]],
     '06': [[0, 6], [0, 7], [1, 6], [2, 7], [2, 8]], '30': [[3, 1], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]],
     '33': [[3, 5], [4, 3], [4, 4], [4, 5], [5, 5]], '36': [[4, 7], [4, 8], [5, 6], [5, 7]],
     '60': [[7, 0], [7, 2], [8, 1]], '63': [[6, 3], [6, 4], [7, 3], [7, 5]],
     '66': [[6, 6], [6, 7], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]}

    possibleNumForCells = {'00': [2, 3, 4], '02': [1, 2, 3, 4, 6], '03': [2, 3, 5, 6, 9], '04': [5, 9], '05': [2, 5, 6, 9],
     '06': [1, 3, 4, 6], '07': [1, 3, 4, 6, 9], '10': [3, 8], '12': [1, 3, 6], '13': [3, 6, 8, 9], '15': [6, 8, 9],
     '16': [1, 3, 6], '21': [2, 3, 6, 8], '22': [2, 3, 4, 6], '23': [2, 3, 6, 8], '27': [3, 4, 6], '28': [3, 6],
     '31': [2, 8], '35': [2, 8], '41': [1, 3, 8], '42': [1, 3, 4, 9], '43': [5, 8, 9], '44': [5, 8, 9],
     '45': [4, 5, 8, 9], '47': [1, 3, 4, 6, 8], '48': [1, 3, 6], '50': [2, 3, 4, 8], '51': [1, 2, 3, 8],
     '52': [1, 2, 3, 4, 9], '55': [2, 4, 8, 9], '56': [1, 3, 4, 8], '57': [1, 3, 4, 8], '63': [5, 6, 8], '64': [5, 8],
     '66': [4, 6, 8], '67': [4, 5, 6, 8], '70': [2, 3], '72': [2, 3, 6], '73': [5, 6, 8, 9], '75': [5, 6, 8, 9],
     '77': [3, 5, 6, 8, 9], '78': [3, 6, 9], '81': [3, 6], '86': [1, 3, 6], '87': [1, 3, 6, 9], '88': [1, 3, 6, 9]}

    eliminate = EliminateCellsInGrid(grid, r_void_cells, c_void_cells, m_grid_void_cells, possibleNumForCells)
    print(eliminate.checkPossibleNumToEliminate())

    for row in grid:
        print(row)

    print(possibleNumForCells)