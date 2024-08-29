'''
在给定的网格中，每个单元格可以有以下三个值之一：


值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。


返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1
'''
from typing import List
'''
一开始，我们找出所有腐烂的橘子，将它们放入队列，作为第 0 层的结点。
然后进行 BFS 遍历，每个结点的相邻结点可能是上、下、左、右四个方向的结点，注意判断结点位于网格边界的特殊情况。
由于可能存在无法被污染的橘子，我们需要记录新鲜橘子的数量。在 BFS 中，每遍历到一个橘子（污染了一个橘子），就将新鲜橘子的数量减一。如果 BFS 结束后这个数量仍未减为零，说明存在无法被污染的橘子
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #在此之间填写代码
        #存放矩阵横竖长度和宽度
        a,b = len(grid),len(grid[0])
        #存放为被感染的橘子数量
        t = 0 
        #存放接下来需要遍历的橘子坐标
        queue = [] 
        for i in range(a):
            for j in range(b):
                #腐烂橘子  该点加入queue列表中
                if grid[i][j]==2:queue.append((i,j)) 
                #新鲜橘子，记录新鲜橘子的数量
                if grid[i][j]==1: t+=1 
        #第一轮腐烂橘子的数量
        m=len(queue) 
        if t==0:return 0 
        #记录到此波为止腐烂橘子的数量
        k = m 
        #存放当前轮数
        n = 0 
        #for循环遍历queue中腐烂橘子的横竖索引
        for x,y in queue:
            #腐烂扩散的方向
            for i,j in ((1,0),(0,1),(-1,0),(0,-1)):
                #扩散的点横竖坐标是否在矩阵内且该处是否有新鲜橘子
                if 0<=x+i<a and 0<=y+j<b and grid[x+i][y+j]==1:
                    #橘子变成腐烂橘子
                    grid[x+i][y+j] = 2
                    #新鲜橘子数量减1 
                    t -= 1 
                    queue.append((x+i,y+j)) 
            m -= 1 
            if m == 0:
                if t==0:return n 
                n += 1 
                m = len(queue) - k 
                k = len(queue) 
        return -1 

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(Solution().orangesRotting([[0,2]]))











































































