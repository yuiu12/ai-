from typing import List
class Solution:
    def romanToInt(self, s: str) -> int:
        #在此之间填写代码
        a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        b={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        x,i = 0,0 
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in b:
                x += b[s[i:i+2]] 
                i += 2 
            else:
                x += a[s[i]] 
                i += 1 
        return x 

print(Solution().romanToInt("III"))
print(Solution().romanToInt("IV"))
print(Solution().romanToInt("IX"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))







































































