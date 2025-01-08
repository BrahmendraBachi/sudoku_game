from sudokuGrids.easy import easyGrids
from sudokuGrids.medium import mediumGrids
from sudokuGrids.hard import hardGrids
from sudokuGrids.expert import expertGrids

import time

def checkGrid(numArr, i, j, num):
    r = (i // 3) * 3
    c = (j // 3) * 3
    for x in range(r, r + 3):
        for y in range(c, c + 3):
            if numArr[x][y] == num:
                return False
    return True


def checkRow(numArr, i, j, num):
    return num not in numArr[i]


def checkColumn(numArr, i, j, num):
    for col in range(9):
        if numArr[col][j] == num:
            return False
    return True


def checkNumber(numArr, i, j, num):
    return checkRow(numArr, i, j, num) and checkColumn(numArr, i, j, num) and checkGrid(numArr, i, j, num)


def checkSudoku(numArr):
    for i in range(9):
        for j in range(9):
            if numArr[i][j] == 0:
                return False
    return True


def giveSuduko(numArr, a=0, b=0, num=0):
    if num != 0:
        numArr[a][b] = num
        if b < 8:
            b = b + 1
        elif b == 8 and a < 8:
            b = 0
            a = a + 1
        else:
            return numArr
    for i in range(a, 9):
        for j in range(b, 9):
            if numArr[i][j] == 0:
                for val in range(1, 10):
                    if checkNumber(numArr, i, j, val):
                        giveSuduko(numArr, i, j, val)
                        if checkSudoku(numArr):
                            return numArr
                        numArr[i][j] = 0

            if numArr[i][j] == 0:
                return
        b = 0
    return numArr


numStr = "3 8 5 0 0 0 0 0 0 " \
         "9 2 1 0 0 0 0 0 0 " \
         "6 4 7 0 0 0 0 0 0 " \
         "0 0 0 1 2 3 0 0 0 " \
         "0 0 0 7 8 4 0 0 0 " \
         "0 0 0 6 9 5 0 0 0 " \
         "0 0 0 0 0 0 8 7 3 " \
         "0 0 0 0 0 0 9 6 2 " \
         "0 0 0 0 0 0 1 4 5".split(" ")
# numStr1 = " 0 0 0 1 2 3 0 0 0 0 0 0 7 8 4 0 0 0 0 0 0 6 9 5 0 0 0 0 0 0 0 0 0 8 7 3 0 0 0 0 0 0 9 6 2 0 0 0 0 0 0 1 4 5"
if __name__ == '__main__':
    st = time.time()
    arr = []
    for i in range(9):
        arr.append(numStr[i * 9: (i * 9) + 9])
    numArr = []
    for i in range(0, 9):
        dum = []
        for j in range(0, 9):
            dum.append(int(arr[i][j]))
        numArr.append(dum)

    grid = numArr
    giveSuduko(numArr)

    for i in grid:
        print(i)
