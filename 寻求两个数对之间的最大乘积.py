'''
两个数对 (a, b) 和 (c, d) 之间的 乘积差 定义为 (a * b) - (c * d) 。
例如，(5, 6) 和 (2, 7) 之间的乘积差是 (5 * 6) - (2 * 7) = 16 。
给你一个整数数组 nums ，选出四个 不同的 下标 w、x、y 和 z ，使数对 (nums[w], nums[x]) 和 (nums[y], nums[z]) 之间的 乘积差 取到 最大值 。
返回以这种方式取得的乘积差中的 最大值 。
输入：nums = [5,6,2,7,4]
输出：34
解释：可以选出下标为 1 和 3 的元素构成第一个数对 (6, 7) 以及下标 2 和 4 构成第二个数对 (2, 4)
乘积差是 (6 * 7) - (2 * 4) = 34
'''
#方法1
def PoorProduct(nums):
    max_1 = max(nums) 
    nums.remove(max_1) 
    max_2 = max(nums) 
    min_1 = min(nums) 
    nums.remove(min_1) 
    min_2 = min(nums) 
    poorproduct = int(max_1) * int(max_2) - int(min_1) * int(min_2) 
    return poorproduct 
a = input('请输入一组数字，中间用逗号隔开:') 
nums1 = a.split(',') 
nums = [] 
for i in nums1:
    nums.append(int(i)) 
print(PoorProduct(nums))

#方法二
a = input("请输入一组数字，中间用逗号隔开:") 
nums1 = a.split(',') 
nums = [] 
for i in nums1:
    nums.append(int(i)) 
nums.sort() 
print(nums[-1]*nums[-2] - nums[0]*nums[1])