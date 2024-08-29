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
            node =  node.next 
        return a 

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #在此填写代码
        a,b = None,head 
        while b:
            c = b.next 
            b.next = a 
            a = b 
            b = c 
        return a 

if __name__ == '__main__':
    print(LinkList().printlist(Solution().reverseList(LinkList().initList([1,2,3,4,5]))))
    print(LinkList().printlist(Solution().reverseList(LinkList().initList([1,2]))))
    print(LinkList().printlist(Solution().reverseList(LinkList().initList([]))))

















