'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #在此之间填写代码
        #暂时存放nums中的第一个元素
        candidate = nums[0] 
        #记录数量
        count = 1
        #for循环变量nums中的所有元素 
        for i in range(1,len(nums)):
            if candidate == nums[i]:
                count += 1 
            else:
                if count == 0:
                    candidate = nums[i] 
                    count = 1 
                else:
                    count -= 1 
        return candidate 

print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))

'''
摩尔投票法
摩尔投票法的基本思想很简单，在每一轮投票过程中，从数组中找出一对不同的元素，将其从数组中删除。
这样不断的删除直到无法再进行投票，如果数组为空，则没有任何元素出现的次数超过该数组长度的一半。
如果只存在一种元素，那么这个元素则可能为目标元素。


那么有没有可能出现最后有两种或两种以上元素呢？
根据定义，这是不可能的，因为如果出现这种情况，则代表我们可以继续一轮投票。
因此，最终只能是剩下零个或一个元素。
'''

















































