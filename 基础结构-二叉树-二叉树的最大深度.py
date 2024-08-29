from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def list_to_binarytree(nums):
    if nums==[]:return 
    b=root=TreeNode(nums[0])
    a=[]
    i=1
    while i < len(nums):
        if nums[i]:
            root.left=TreeNode(nums[i])
            a.append(root.left)
        if i+1<len(nums):
            if nums[i+1]:
                root.right=TreeNode(nums[i+1])
                a.append(root.right)
        i+=2
        root=a.pop(0)
    return b


root = list_to_binarytree([1,None,2,3,None,4,5,6,7,8])
'''
要求最大深度1，可以求出每条树枝的长度，最终取出最大值
当节点为None时，深度为0
若有子树，则子树头结点深度加1，直到没有子树为止
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #在此填写代码
        if not root:return 0 
        else:
            return max(self.maxDepth(root.right),self.maxDepth(root.left)) + 1 
        

print(Solution().maxDepth(list_to_binarytree([1,None,2,3])))
print(Solution().maxDepth(list_to_binarytree([])))
print(Solution().maxDepth(list_to_binarytree([1])))
print(Solution().maxDepth(list_to_binarytree([1,2])))
print(Solution().maxDepth(list_to_binarytree([1,None,2])))
