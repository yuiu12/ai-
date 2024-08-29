from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #在此之间填写代码
        #每个组合和组合中的数字
        res,path = [],[] 
        #赋值从1到n的列表
        m = list(range(1,n+1))
        #内部变量初始列表以及后面要求的列表以及限制条件
        def backtrack(a,res,path,k):
            #此时path里面的元素数量已经满足条件
            if k == 0:
                #放进res列表在
                res.append(path[:])
            #存放初始列表长度
            x = len(a)
            for i in range(x):
                #初始列表中删除第一个元素
                b = a.pop(i) 
                #并赋值给b
                path.append(b) 
                backtrack(a[i:],res,path,k-1)
                path.pop() 
                a.insert(i,b) 
        backtrack(m,res,path,k) 
        return res 

print(Solution().combine(4,2))
print(Solution().combine(1,1))

'''
如果解决一个问题有多个步骤，每一个步骤有多种方法，题目又要我们找出所有的方法，可以使用回溯算法；
回溯算法是在一棵树上的 深度优先遍历（因为要找所有的解，所以需要遍历）；
组合问题，相对于排列问题而言，不计较一个组合内元素的顺序性（即 [1, 2, 3] 与 [1, 3, 2] 认为是同一个组合），因此很多时候需要按某种顺序展开搜索，这样才能做到不重不漏。
'''


























































































