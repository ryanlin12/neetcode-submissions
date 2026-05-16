from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #use set for duplicates
        
        #each key is a row
        #each value in the set is a column element
        columnarray = [set() for i in range(9)]
        rowSet = set()
        sodokuSquares = defaultdict(set)
        rowNum = 0
        squareCoord = (0, 0)
        for rowNum, row in enumerate(board):
            rowSet.clear()
            
            for colNum, num in enumerate(row):
                #checking row duplicates
                #print(colNum)
                if num.isdigit():
                    if num in rowSet:
                        return False
                    rowSet.add(num)
                    

                #checking column duplicates
                #print(columnarray)

                #print(colNum)
                if num.isdigit():
                    if num in columnarray[colNum]:
                        return False
                    columnarray[colNum].add(num)

                #checking square duplicates
                squareNum = ((rowNum // 3), (colNum // 3))
                if num.isdigit():
                    if num in sodokuSquares[squareNum]:
                        return False
                    sodokuSquares[squareNum].add(num)

            #print(rowSet)
        print(sodokuSquares)
                

        return True