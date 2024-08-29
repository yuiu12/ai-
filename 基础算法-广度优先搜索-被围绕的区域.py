'''
从边界出发吧，先把边界上和 O 连通点找到, 把这些变成 B
然后遍历整个 board 把 O 变成 X, 把 B 变成 O
'''
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #在此之间填写代码
        #长度和宽度
        a,b = len(board),len(board[0]) 
        #存放接下来需要遍历的坐标
        queue = [] 
        #遍历矩阵边界的点的坐标
        i,x = 0,0 
        while i < a:
            if board[i][x]=='O':queue.append((i,x)) 
            i += 1 
            if i==a and x != b-1:
                i = 0 
                x = b - 1 
        i,x = 0,0 
        while i < b:
            if board[x][i]=='O':queue.append((x,i)) 
            i += 1 
            if i == b and x != a-1:
                i=0 
                x = a - 1 
        while queue:
            cur = queue.pop(0) 
            for i in ((1,0),(0,1),(-1,0),(0,-1)):
                x,y = cur[0]+i[0],cur[1]+i[1] 
                if 0<=x<a and 0<=y<b and board[x][y]=='O':
                    queue.append((x,y)) 
            board[cur[0]][cur[1]]='B'
        for i in range(a):
            for j in range(b):
                if board[i][j]=='O':board[i][j]='X'
                if board[i][j]=='B':board[i][j]='O'
        return board 
    

print(Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
print(Solution().solve([["X"]]))
print(Solution().solve([["O","O"],["O","O"]]))































































































