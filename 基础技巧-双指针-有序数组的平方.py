from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #在此之间填写代码
        #前指针fd赋值为0，定义变量a复制列表的长度
        fd,a = 0,len(nums) 
        #列表中第一个大于等于0的元素并将其索引赋值给fd，若没找到，则遍历到最后
        while fd < a:
            if nums[fd] >= 0:
               break 
            fd += 1 
            #前指针fd，后指针bk 赋值fd和fd-1
            fd,bk = fd,fd - 1 
            #空列表存放排列后的结果
            m = [] 
            while fd < a or bk > -1:
                if fd == a or (fd < a and bk > -1 and nums[fd]>=-nums[bk]):
                    m.append(nums[bk]**2) 
                    bk -= 1 
                else:
                    m.append(nums[fd]**2) 
                    fd += 1 
            return m 

print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-7,-3,2,3,11]))
'''
如果数组 nums 中的所有数都是非负数，那么将每个数平方后，数组仍然保持升序；
如果数组 nums 中的所有数都是负数，那么将每个数平方后，数组会保持降序。
如果我们能够找到数组 nums 中负数与非负数的分界线，那么就可以用类似「归并排序」的方法了。
具体地，使用两个指针分别指向位置 neg 和 neg-1，每次比较两个指针对应的数，选择较小的那个放入答案并移动指针。
当某一指针移至边界时，将另一指针还未遍历到的数依次放入答案。
'''


























































































