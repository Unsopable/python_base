class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
    
        #### 双指针(slow和fast指针) 【注意判断两节点（指针）是否相等（相同）直接用 == 号 或 is 都行了】
        ## 先让fast 和 slow 指针都指向头节点
        slow,fast = head,head

        ## while循环，迭代链表【条件slow 与 fast 不相遇】
        while True:

            ### 如果fast和fast.next其中一个为None则表示链表没有环，返回None
            if not (fast and fast.next): return None
            
            ## slow走一步
            slow = slow.next
            ## fast走两步
            fast = fast.next.next

            ### 如果 slow 和 fast 相遇，则退出循环
            if slow == fast:
                break
            

        ###### 退出上一个while循环，表示slow和 fast相遇了
        ##### 我们让fast重新 回到头节点，slow不动，然后slow和fast以相同的速度再走。再次相遇就是环的头节点位置
        fast = head
        ### fast 从头开始走
        while (fast != slow):
            fast = fast.next
            slow = slow.next

        return fast