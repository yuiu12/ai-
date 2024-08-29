#二分查找
class Solution:
    def mySqrt(x: int) -> int:
        #在此之间填写代码
        i,j = 1,x 
        while i <= j:
            m = (i + j) // 2 
            if m * m <= x:i=m+1 
            elif m*m>x:j=m-1 
        return j 

if __name__ == "__main__":
    print(Solution.mySqrt(4))
    print(Solution.mySqrt(8))
    print(Solution.mySqrt(18372836))

#方法二 顺序查找
class Solution:
    def mySqrt(x: int) -> int:
        #在此之间填写代码
        i = 1 
        while i * i <= x:
            i += 1 
        return i - 1 

if __name__ == "__main__":
    print(Solution.mySqrt(4))
    print(Solution.mySqrt(8))
    print(Solution.mySqrt(18372836))
