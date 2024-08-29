class ListNode:
    def __init__(self,x):
        self.val = x 
        self.next = None 
    
class LinkList:
    def __init__(self):
        self.head = None 
    
    def initList(self,data):
        while len(data)==0:return None 
        self.head = ListNode(data[0]) 
        r = self.head 
        p = self.head 
        for i in data[1:]:
            node = ListNode(i) 
            p.next = node 
            p = p.next 
        return r 
    def printlist(self,head):
        a = [] 
        if head == None: return [] 
        node = head 
        while node != None:
            a.append(node.val) 
            node = node.next 
        return a 

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #在此填写代码
        a = [] 
        while head:
            a.append(head.val) 
            head = head.next 
        return a==a[::-1] 

if __name__ == '__main__':
    print(Solution().isPalindrome(LinkList().initList([1,2,2,1])))
    print(Solution().isPalindrome(LinkList().initList([1,2])))
    print(Solution().isPalindrome(LinkList().initList([])))
