'''
值大小，数值在 0 到 65535 之间。
给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。
最后返回经过上色渲染后的图像。
'''
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #在此之间填写代码
        a = image[sr][sc] 
        if a == newColor:return image 
        image[sr][sc] = newColor 
        x = [(1,0),(0,1),(-1,0),(0,-1)] 
        queue = [(sr,sc)] 
        while queue:
            cur = queue.pop(0) 
            for i in x:
                m,n = cur[0]+i[0],cur[1]+i[1] 
                if 0<=m<len(image) and 0<=n<len(image[0]) and image[m][n] == a:
                    image[m][n] = newColor 
                    queue.append((m,n)) 
            return image 

print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))




























