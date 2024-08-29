'''
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。
整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x
'''
from typing import List
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #在此之间填写代码
        if n==0:return False 
        if n==1:return True 
        return n%3==0 and self.isPowerOfThree(n/3)

print(Solution().isPowerOfThree(27))
print(Solution().isPowerOfThree(0))
print(Solution().isPowerOfThree(9))
print(Solution().isPowerOfThree(1))
'''
判断该数是否可以整除3，若可以，再判断除以3后得到的数是否也可以整除3
若可以一直下去直到结果为1，则返回True
其他情况则返回False
'''
'''
什么是递归
程序调用自身的编程技巧称为递归
递归做为一种算法在程序设计语言中广泛应用。


递归算法一般用于解决三类问题：
(1)数据的定义是按递归定义的。（Fibonacci函数）
(2)问题解法按递归算法实现。
(3)数据的结构形式是按递归定义的。


递归函数特征
必须有一个明确的结束条件；
每次进入更深一层递归时，问题规模相比上次递归都应有所减少
相邻两次重复之间有紧密的联系，前一次要为后一次做准备（通常前一次的输出就作为后一次的输入）。
递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）
'''













































