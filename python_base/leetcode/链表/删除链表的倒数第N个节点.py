class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #### 方法一：暴力破解法
        ## 计算 链表 的长度
        ln = 0
        curr = head
        while (curr != None):
            ln += 1
            curr = curr.next

            #### 找到顺序 的 第几个 节点
        order_n = (ln - n)

        ### 特殊情况 n 为 最后一个
        if order_n == 0:
            return head.next

        ### 其他情况
        pre = head ### pre 和 head 指向的 内存地址 是一样地。所有，改变pre.next 也就 改变了 head.next
        for i in range(order_n - 1):
            pre = pre.next
        pre.next = pre.next.next
        return head

node4 = ListNode(5,None)
node3 = ListNode(4,node4)
node2 = ListNode(3,node3)
node1 = ListNode(2,node2)
head = ListNode(1,node1)

s = Solution()
res = s.removeNthFromEnd(head,3)
