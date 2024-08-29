'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
class LinkList:
    def __init__(self):
        self.head=None
 
    def initList(self, data):
        while len(data)==0:return None
        self.head = ListNode(data[0])
        r=self.head
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r
    def printlist(self,head):
        a=[]
        if head == None: return []
        node = head
        while node != None:
            a.append(node.val)
            node = node.next
        return a
class Solution:
    def mergeTwoLists(self,l1: ListNode, l2: ListNode) -> ListNode:
        #在此填写代码
        import math 
        if not l1 and not l2:return
        #math.inf无穷大
        if (l1.val if l1 else math.inf) < (l2.val if l2 else math.inf):
            node = ListNode(l1.val) 
            node.next = self.mergeTwoLists(l1.next,l2) 
        else:
            node = ListNode(l2.val) 
            node.next = self.mergeTwoLists(l1,l2.next) 
        return node 

if __name__ == '__main__':
    print(LinkList().printlist(Solution().mergeTwoLists(LinkList().initList([1,2,4]),LinkList().initList([1,3,4]))))
    print(LinkList().printlist(Solution().mergeTwoLists(LinkList().initList([]),LinkList().initList([]))))
    print(LinkList().printlist(Solution().mergeTwoLists(LinkList().initList([]),LinkList().initList([0]))))






































