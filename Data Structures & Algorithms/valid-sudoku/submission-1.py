from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnarray = [set() for i in range(9)]
        rowSet = set()
        sodokuSquares = defaultdict(set)
        rowNum = 0
        squareCoord = (0, 0)
        for rowNum, row in enumerate(board):
            rowSet.clear()
            for colNum, num in enumerate(row):
                squareNum = ((rowNum // 3), (colNum // 3))
                if num.isdigit():
                    if num in rowSet:
                        return False
                    rowSet.add(num)
                    if num in columnarray[colNum]:
                        return False
                    columnarray[colNum].add(num)
                    if num in sodokuSquares[squareNum]:
                        return False
                    sodokuSquares[squareNum].add(num)
        return True