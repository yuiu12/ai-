'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
有效括号组合需满足：左括号必须以正确的顺序闭合。
'''
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #在此之间填写代码
        a = [] 
        b = '' 
        def x(b,i,j):
            if i==j==n:a.append(b[:]) 
            if i<j:return 
            if i<=n:
                x(b+'(',i+1,j) 
            if j<=n:
                x(b+')',i,j+1) 
        x(b,0,0) 
        return a 

print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(1))











































