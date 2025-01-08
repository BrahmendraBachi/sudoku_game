class EliminateNumbers:

    def __init__(self, r_void_cells, c_void_cells, m_grid_void_cells, possibleNumForCells):
        self.r_void_cells = r_void_cells
        self.c_void_cells = c_void_cells
        self.m_grid_void_cells = m_grid_void_cells
        self.possibleNumForCells = possibleNumForCells
        self.k_strs = ["00", "03", "06", "30", "33", "36", "60", "63", "66"]

    # def __init__(self, possibleNumForCells):
    #     self.possibleNumForCells = possibleNumForCells



    def getVoidCellsInRow(self):
        cellAndValuesInRow = {}
        numsInRow = []
        eliminatedNums = []
        foundNum = 0
        for row in self.r_void_cells:
            for cell in self.r_void_cells[row]:
                cell = str(cell[0]) + str(cell[1])
                cellAndValuesInRow[cell] = self.possibleNumForCells[cell]
                for num in self.possibleNumForCells[cell]:
                    if num in eliminatedNums:
                        continue
                    elif num in numsInRow:
                        foundNum -= num
                        eliminatedNums.append(num)
                    else:
                        foundNum += num
                        numsInRow.append(num)


            self.checkElimination(cellAndValuesInRow, numsInRow)


            numsInRow = []
            cellAndValuesInRow = {}



    def getVoidCellsInCol(self):
        cellAndValuesInCol = {}
        numsInCell = []
        for col in self.c_void_cells:
            for cell in self.c_void_cells[col]:
                cell = str(cell[0]) + str(cell[1])
                cellAndValuesInCol[cell] = self.possibleNumForCells[cell]
                for num in self.possibleNumForCells[cell]:
                    numsInCell.append(num)
            numsInCell = []
            cellAndValuesInCol = {}

    def checkElimination(self):
        pass

if __name__ == '__main__':
    r_void_cells = {0: [[0, 1], [0, 2], [0, 3], [0, 4], [0, 7]], 1: [[1, 0], [1, 1], [1, 4], [1, 5], [1, 7]],
     2: [[2, 0], [2, 2], [2, 4], [2, 7]], 3: [[3, 2], [3, 3], [3, 6], [3, 7], [3, 8]],
     4: [[4, 0], [4, 2], [4, 5], [4, 6], [4, 8]], 5: [[5, 0], [5, 1], [5, 2], [5, 3], [5, 5]],
     6: [[6, 1], [6, 4], [6, 6], [6, 8]], 7: [[7, 3], [7, 4], [7, 6], [7, 8]],
     8: [[8, 0], [8, 1], [8, 4], [8, 5], [8, 6], [8, 7]]}

    c_void_cells = {0: [[1, 0], [2, 0], [4, 0], [5, 0], [8, 0]], 1: [[0, 1], [1, 1], [5, 1], [6, 1], [8, 1]],
     2: [[0, 2], [2, 2], [3, 2], [4, 2], [5, 2]], 3: [[0, 3], [3, 3], [5, 3], [7, 3]],
     4: [[0, 4], [1, 4], [2, 4], [6, 4], [7, 4], [8, 4]], 5: [[1, 5], [4, 5], [5, 5], [8, 5]],
     6: [[3, 6], [4, 6], [6, 6], [7, 6], [8, 6]], 7: [[0, 7], [1, 7], [2, 7], [3, 7], [8, 7]],
     8: [[3, 8], [4, 8], [6, 8], [7, 8]]}

    m_grid_void_cells = {'00': [[0, 1], [0, 2], [1, 0], [1, 1], [2, 0], [2, 2]], '03': [[0, 3], [0, 4], [1, 4], [1, 5], [2, 4]],
     '06': [[0, 7], [1, 7], [2, 7]], '30': [[3, 2], [4, 0], [4, 2], [5, 0], [5, 1], [5, 2]],
     '33': [[3, 3], [4, 5], [5, 3], [5, 5]], '36': [[3, 6], [3, 7], [3, 8], [4, 6], [4, 8]],
     '60': [[6, 1], [8, 0], [8, 1]], '63': [[6, 4], [7, 3], [7, 4], [8, 4], [8, 5]],
     '66': [[6, 6], [6, 8], [7, 6], [7, 8], [8, 6], [8, 7]]}

    possibleNumForCells = {'01': [3, 5, 7], '02': [1, 3, 5, 7], '03': [3, 7, 9], '04': [1, 3, 9], '07': [7, 9], '10': [1, 4, 7], '11': [4, 6, 7], '14': [1, 4, 9], '15': [1, 4, 7, 9], '17': [6, 7, 9], '20': [3, 4, 7], '22': [3, 6, 7], '24': [3, 4], '27': [6, 7], '32': [1, 3, 5, 6, 7], '33': [3, 6], '35': [1, 3, 4], '36': [5, 6, 7], '37': [3, 5, 6, 7], '38': [1, 3, 6, 7], '40': [1, 3, 7], '42': [1, 3, 6, 7], '45': [1, 3, 9], '46': [6, 7, 9], '48': [1, 3, 6, 7, 9], '50': [1, 3, 4, 5], '51': [3, 4, 5, 6], '52': [1, 3, 5, 6], '53': [3, 6, 9], '55': [1, 3, 4, 9], '61': [3, 5, 7], '64': [2, 3], '66': [2, 5, 7], '68': [3, 7], '73': [3, 6, 7, 9], '74': [3, 6, 9], '76': [6, 7, 9], '78': [3, 6, 7, 9], '80': [3, 5, 7], '81': [3, 5, 7], '84': [2, 3, 6, 9], '85': [3, 7, 9], '86': [2, 5, 6, 7, 9], '87': [3, 5, 6, 7, 9]}

    eliminate = EliminateNumbers(r_void_cells, c_void_cells, m_grid_void_cells, possibleNumForCells)

    eliminate.getVoidCellsInRow()

    print(possibleNumForCells)