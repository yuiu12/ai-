'''
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。
'''
from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #在此之间填写代码
        j = 0 
        a,b = len(haystack),len(needle) 
        if b==0:return 0 
        while j < a:
            if haystack[j:j+b]==needle:
                return j 
            j += 1 
        return -1 

print(Solution().strStr("hello","ll"))
print(Solution().strStr("aaaaa", needle = "bba"))
print(Solution().strStr(haystack = "", needle = ""))
































































