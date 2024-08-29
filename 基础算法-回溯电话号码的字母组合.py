from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #在此之间填写代码
        if not digits:return [] 
        a = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

        def backtrack(an,bn):
            if len(bn)==0:
                res.append(an) 
            else:
                for x in a[bn[0]]:
                    backtrack(an+x,bn[1:]) 
        res = [] 
        backtrack('',digits) 
        return res 

print(Solution().letterCombinations("23"))
print(Solution().letterCombinations(""))
print(Solution().letterCombinations("2"))


'''
首先使用哈希表存储每个数字对应的所有可能的字母，然后进行回溯操作。
回溯过程中维护一个字符串，表示已有的字母排列（如果未遍历完电话号码的所有数字，则已有的字母排列是不完整的）
该字符串初始为空。每次取电话号码的一位数字，从哈希表中获得该数字对应的所有可能的字母，并将其中的一个字母插入到已有的字母排列后面，然后继续处理电话号码的后一位数字，直到处理完电话号码中的所有数字，即得到一个完整的字母排列。
然后进行回退操作，遍历其余的字母排列。
回溯算法用于寻找所有的可行解，如果发现一个解不可行，则会舍弃不可行的解。在这道题中，由于每个数字对应的每个字母都可能进入字母组合，因此不存在不可行的解，直接穷举所有的解即可。
'''




































































































