'''
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
任何误差小于 10-5 的答案都将被视为正确答案。
'''
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #在此之间填写代码
        i,a = 1,len(nums) 
        t=x=sum(nums[0:k]) 
        while i + k < a + 1:
            x=x-nums[i-1]+nums[i+k-1] 
            if t < x:
                t=x 
            i+=1 
        return t/k 

print(Solution().findMaxAverage([1,12,-5,-6,50,3],4))
print(Solution().findMaxAverage([5],1))

'''
先算出数组从0下标到k-1下标之间的和sum, max=sum;
遍历从下标1开始到nums长度-1之间范围的元素，每次sum先减去i-1(上一个元素的值)，再加上i+k-i的值，即窗口内最后一值，再与max作比较；
最终返回平均值
'''
'''
滑动窗口，顾名思义，就是有一个大小可变的窗口，左右两端方向一致的向前滑动（右端固定，左端滑动；左端固定，右端滑动）。
适用范围
- 1、一般是字符串或者列表
- 2、一般是要求最值（最大长度，最短长度等等）或者子序列
算法思想
- 1、在序列中使用双指针中的左右指针技巧，初始化 left = right = 0，把索引闭区间 [left, right] 称为一个窗口。
- 2、先不断地增加 right 指针扩大窗口 [left, right]，直到窗口中的序列符合要求。
- 3、此时，停止增加 right，转而不断增加 left 指针缩小窗口 [left, right]，直到窗口中的序列不再符合要求。同时，每次增加 left前，都要更新一轮结果。
- 4、重复第 2 和第 3 步，直到 right 到达序列的尽头。
思路其实很简单：第 2 步相当于在寻找一个可行解，然后第 3 步在优化这个可行解，最终找到最优解。左右指针轮流前进，窗口大小增增减减，窗口不断向右滑动
'''




















































