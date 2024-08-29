'''
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
'''
from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        #cur添加元素s的全小写形态
        cur=[s.lower()]
        #赋值字符串s的长度
        a=len(s)
        def backtrack(s,m):
            for i in range(m,a):
                #判断字符串中索引i对应的元素是否不是数字
                if s[i] not in ['1','2','3','4','5','6','7','8','9','0']:
                    #该元素变为大写并将字符串添加到列表
                    cur.append(s[:i]+s[i].upper()+s[i+1:])
                    backtrack(s[:i]+s[i].upper()+s[i+1:],i+1)
            return cur
        return backtrack(s.lower(),0)

print(Solution().letterCasePermutation("a1b2"))
print(Solution().letterCasePermutation("3z4"))
print(Solution().letterCasePermutation("12345"))






































































