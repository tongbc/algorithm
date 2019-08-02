class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    isShip = True
                    if(i!=0):
                        if board[i - 1][j] == 'X':
                            isShip = False
                    if(j!=0):
                        if board[i][j-1] == 'X':
                            isShip = False
                    if(isShip):
                        count += 1
        return count