#初始代码
class ListNode:
    def __init__(self,x):
        self.val = x 
        self.next = None 

class LinkList:
    def __init__(self):
        self.head = None 

    def initList(self,data):
        while len(data) == 0: return None 
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
        if head == None:return [] 
        node = head 
        while node != None:
            a.append(node.val) 
            node = node.next 
        return a 
class Solution:
    def mergeTwoLists(self,l1:ListNode,l2:ListNode) -> ListNode:
        #创建初始链表p，头指针数值为0
        p = ListNode(0) 
        #保存头指针于变量q上，移动的是p指针
        q = p 
        while l1 and l2:
            #l1和l2的数值
            if l1.val >= l2.val:
                p.next = l2 
                l2 = l2.next 
            else:
                p.next = l1 
                l1 = l1.next 
            p = p.next 
        p.next = l1 if l1 is not None else l2 
        return q.next 

if __name__ =='__main__':
    print(LinkList().printlist(Solution().mergeTwoLists(LinkList().initList([1,2,4]),LinkList().initList([1,3,4]))))
    print(LinkList().printlist(Solution().mergeTwoLists(LinkList().initList([]),LinkList().initList([]))))
    print(LinkList().printlist(Solution().mergeTwoLists(LinkList().initList([]),LinkList().initList([0]))))