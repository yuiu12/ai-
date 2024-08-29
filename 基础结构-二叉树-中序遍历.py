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

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack,mid=[],[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            mid.append(root.val)
            root=root.right
        return mid

print(Solution().inorderTraversal(list_to_binarytree([1,None,2,3])))
print(Solution().inorderTraversal(list_to_binarytree([])))
print(Solution().inorderTraversal(list_to_binarytree([1])))
print(Solution().inorderTraversal(list_to_binarytree([1,2])))
print(Solution().inorderTraversal(list_to_binarytree([1,None,2])))
