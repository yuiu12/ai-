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
可以使用反向思路，用总长度减去当前根节点的值，若结果等于某条树枝的长度就可以返回True
判断结果是否等于某条树枝的长度，可以再是用原函数，树变为根节点的左或右子树，数值变为减去根节点后剩下的值，递归
只要有路径长度为数值，则可返回True，所以对于所有的叶子结点，用or来判断，若其中一个为True，则返回True
'''
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        #在此填写代码
        if not root:
            return False 
        #将targetSum减去当前节点的值，用于判断其左右子树的长度是否满足题意
        targetSum -= root.val 
        if not (root.right or root.left) and targetSum==0:
            return True 
        else:
            return self.hasPathSum(root.right,targetSum) or self.hasPathSum(root.left,targetSum)


print(Solution().hasPathSum(list_to_binarytree([5,4,8,11,None,13,4,7,2,None,None,None,1]),22))
print(Solution().hasPathSum(list_to_binarytree([1,2,3]),5))
print(Solution().hasPathSum(list_to_binarytree([1,2]),0))












































