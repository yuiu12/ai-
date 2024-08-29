from typing import List 
class TreeNode:
    def __init__(self,x):
        self.val = x 
        self.left = None 
        self.right = None 

def list_to_binarytree(nums):
    if nums==[]:return 
    b=root=TreeNode(nums[0]) 
    a = [] 
    i = 1 
    while i < len(nums):
        if nums[i]:
            root.left = TreeNode(nums[i]) 
            a.append(root.left) 
        if i+1<len(nums):
            if nums[i+1]:
                root.right = TreeNode(nums[i+1]) 
                a.append(root.right) 
        i += 2
        root = a.pop(0) 
    return b 

root = list_to_binarytree([1,None,2,3,None,4,5,6,7,8])

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #在此填写代码
        stark,x = [],[] 
        def a(stark,root,x):
            if root:
                stark.append(root) 
            else:return [] 
            if root.left:a(stark,root.left,x) 
            if root.right:a(stark,root.right,x) 
            x.append(stark.pop().val) 
            return x 
        return a(stark,root,x)

print(Solution().postorderTraversal(list_to_binarytree([1,None,2,3])))
print(Solution().postorderTraversal(list_to_binarytree([])))
print(Solution().postorderTraversal(list_to_binarytree([1])))
print(Solution().postorderTraversal(list_to_binarytree([1,2])))
print(Solution().postorderTraversal(list_to_binarytree([1,None,2])))
































































