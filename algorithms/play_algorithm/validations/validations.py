class Validations:

    def __init__(self, grid):
        self.grid = grid


    def checkGrid(self, i, j, num):
        r = (i // 3) * 3
        c = (j // 3) * 3
        for x in range(r, r + 3):
            for y in range(c, c + 3):
                if self.grid[x][y] == num and x != i and y != j:
                    return False
        return True

    def checkRow(self, i, j, num):
        return num not in self.grid[i]

    def checkColumn(self, i, j, num):
        for row in range(9):
            try:
                if self.grid[row][j] == num and i != row:
                    return False
            except:
                print(self.grid)
        return True

    def checkGridIsZero(self, i, j):
        return not self.grid[i][j]

    def checkNumber(self, i, j, num):
        return self.checkRow(i, j, num) and self.checkColumn(i, j, num) and self.checkGrid(i, j, num) and self.checkGridIsZero(i, j)

    def checkNumber1(self, i, j, num):
        return self.checkRow(i, j, num) and self.checkColumn(i, j, num) and self.checkGrid(i, j, num)
