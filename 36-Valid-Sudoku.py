class Solution(object):
    def isValidSudoku(self, board):
        \\\
        :type board: List[List[str]]
        :rtype: bool
        \\\
        def minifunc(brd):
        
            for s in brd:

                for j in range(len(s)):
                    if s[j] == \.\:
                        s[j]=10*j

                if len(s)!=len(list(set(s))):
                    return False
                
            return True
        
        rotate = []
        for i in range(9):
            lst1 = []
            for j in range(9):
                lst1.append(board[j][i])
            rotate.append(lst1)
            
        smalls = []
        k = 0

        while k<=6:
            x = 0
            while x<=6:
                lst=[]
                for i in range(k, k+3):
                    for j in range(x, x+3):
                        lst.append(board[i][j])


                smalls.append(lst)
                x=x+3 
            k=k+3
                
            
            
        if minifunc(board)==True and minifunc(rotate)==True and minifunc(smalls)==True:
            return True
        else:
            return False