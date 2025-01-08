class NakedPairs:

    def __init__(self, possibleNumForCells):
        self.possibleNumForCells = possibleNumForCells

    def updatePossibleNumForCells(self):
        isUpdated = False
        for i in range(9):
            row = {}
            col = {}
            for j in range(9):

                cell_r = str(i) + str(j)
                if cell_r in self.possibleNumForCells:
                    row[cell_r] = self.possibleNumForCells[cell_r]

                cell_c = str(j) + str(i)
                if cell_c in self.possibleNumForCells:
                    col[cell_c] = self.possibleNumForCells[cell_c]

            if len(row) > 2:
                isUpdated = self.checkGrid(row) or isUpdated
            if len(col) > 2:
                isUpdated = self.checkGrid(col) or isUpdated

        return self.updatePossibleNumForGrids() or isUpdated
                

    def checkGrid(self, grid):

        isUpdated = False

        for cell_1 in grid:
            temp_cell = cell_1
            nums1 = self.possibleNumForCells[cell_1]
            if len(nums1) > 2:
                continue
            for cell_2 in grid:
                nums2 = self.possibleNumForCells[cell_2]
                if cell_2 != temp_cell and nums1 == nums2:
                    isUpdated = self.updateGrid(nums1, grid) or isUpdated
        return isUpdated

    def updateGrid(self, nums, grid):
        isUpdated = False
        for cell in grid:
            if self.possibleNumForCells[cell] == nums:
                continue
            for num in nums:
                if num in self.possibleNumForCells[cell]:
                    self.possibleNumForCells[cell].remove(num)
                    isUpdated = True
        return isUpdated
    
    def updatePossibleNumForGrids(self):
        isUpdated = False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = self.getGrid(i, j)
                if len(grid) > 2:
                   isUpdated = self.checkGrid(grid) or isUpdated
        return isUpdated
                    
                    
    def getGrid(self, x, y):
        grid = {}
        for r in range(x, x + 3):
            for c in range(y, y + 3):
                cell = str(r) + str(c)
                if cell in self.possibleNumForCells:
                    grid[cell] = self.possibleNumForCells[cell]

        return grid
                    
    
                
                    

# if __name__ == '__main__':
#     possibleNumForCells = {'01': [7, 8], '06': [7, 8], '12': [5, 7, 8], '13': [3, 5, 7], '14': [7, 8], '15': [3, 5, 7, 8], '17': [2, 9], '18': [2, 7, 9], '22': [5, 7, 8], '23': [1, 5, 7], '25': [1, 5, 7, 8], '26': [7, 8], '30': [4, 5, 8], '31': [1, 2, 5, 8], '32': [4, 5, 8], '33': [1, 5], '36': [3, 4, 5], '38': [2, 3], '40': [5, 7, 9], '43': [5, 7], '45': [2, 5, 7], '47': [2, 5, 9], '50': [4, 5, 7, 9], '51': [1, 2, 5, 7], '52': [4, 5, 7, 9], '55': [1, 2, 5, 7], '56': [4, 5, 9], '57': [2, 4, 5, 9], '60': [5, 7, 8, 9], '61': [5, 6, 7, 8], '63': [3, 6, 7, 9], '64': [7, 8], '66': [3, 5, 7, 9], '67': [5, 6, 9], '71': [6, 7, 8], '75': [7, 8], '76': [4, 7, 9], '77': [4, 6, 9], '78': [7, 9], '80': [4, 5, 7, 9], '81': [5, 6, 7], '82': [4, 5, 7, 9], '83': [3, 6, 7, 9], '85': [3, 7], '88': [3, 7, 9]}
#     nakedPairCheck = NakedPairs(possibleNumForCells)
#     print(nakedPairCheck.updatePossibleNumForCells())
#     print(nakedPairCheck.possibleNumForCells)

