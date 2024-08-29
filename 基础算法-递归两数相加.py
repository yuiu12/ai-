'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
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
'''
根据题意可知链表数字位数是从小到大的
因为两个数字相加会产生进位，所以使用i来保存进位。
则当前位的值为(l1.val + l2.val + i) % 10
则进位值为(l1.val + l2.val + i) / 10
建立新node，然后将进位传入下一层。
'''   
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #在此之间填写代码
        #内部变量l，r，i分别代表第一个链表，第二个链表已经它们和的十位数
        def dfs(l,r,i):
            if not l and not r and not i:return None 
            #变量s，链表存在，加上链表该位置的值，不存在加0，加上i的值
            s = (l.val if l else 0) + (r.val if r else 0) + i 
            #和的个位数
            node = ListNode(s % 10) 
            #node的下一个元素进行递归操作，内部变量分别为之前两个链表的后一个元素以及刚刚和的十位数
            node.next = dfs(l.next if l else None,r.next if r else None,s // 10) 
            return node 
        return dfs(l1,l2,0) 

if __name__ == '__main__':
    print(LinkList().printlist(Solution().addTwoNumbers(LinkList().initList([2,4,3]),LinkList().initList([5,6,4]))))
    print(LinkList().printlist(Solution().addTwoNumbers(LinkList().initList([0]),LinkList().initList([0]))))
    print(LinkList().printlist(Solution().addTwoNumbers(LinkList().initList([9,9,9,9,9,9,9]),LinkList().initList([9,9,9,9]))))


































































