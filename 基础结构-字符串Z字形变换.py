'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
'''

from typing import List
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #在此之间填写代码
        if numRows==1:return s 
        else:n,b,c,y=0,0,0,[] 
        while b < numRows:
            try:
                y.append(s[n]) 
            except:
                b +=1 
            if b==0 or b==numRows-1:n+=(numRows-1)*2 
            else:
                if c % 2==0:n+=((numRows-1)*2-2*b) 
                else:n+=(2*b) 
            c+=1 
            if n >= len(s):
                b += 1 
                n,c = b,0 
        return ''.join(y)

print(Solution().convert("PAYPALISHIRING",3))
print(Solution().convert("PAYPALISHIRING",4))
print(Solution().convert("A",1))











































