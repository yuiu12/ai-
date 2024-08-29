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
        if head == None:return [] 
        node = head 
        while node != None:
            a.append(node.val) 
            node = node.next 
        return a 

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        b = ListNode(0) 
        c = b 
        while head:
            c.next = head 
            while head.next and head.val == head.next.val:
                head.next = head.next.next 
            head = head.next 
            c = c.next 
        return b.next 

if __name__ == '__main__':
    print(LinkList().printlist(Solution().deleteDuplicates(LinkList().initList([1,1,2]))))
    print(LinkList().printlist(Solution().deleteDuplicates(LinkList().initList([1,1,2,3,3]))))
    print(LinkList().printlist(Solution().deleteDuplicates(LinkList().initList([]))))