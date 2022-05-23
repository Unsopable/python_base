
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # ##### 方法一：迭代
        # curr = head
        # #### 最后返回pre
        # pre = None
        # ### 如果节点不为空，则继续循环
        # while(curr):
        #     ## 三个变量，存储当前节点，下一个节点，前节点
        #     next = curr.next

        #     ## 将当前节点的下一个节点指向上一个节点，完成翻转
        #     curr.next = pre
            
        #     ## 进行下一次反转，当前节点变为前节点
        #     pre = curr

        #     ## 当前节点变为下一个节点
        #     curr = next

        # return pre

        
        ######## 方法二：递归【找到最后一个节点，从后向前迭代】
        ## 定义递归函数
        def dg(head):
            ### 递归出口
            #### 如果head为空，则直接返回，如果head.next为空也返回
            if(not head or not head.next):
                return head
           
            #### 找到最后一个节点【注意有返回值，返回的是输入链表的最后一个节点，也是反转后新链表的头节点】
            new_head = dg(head.next)
            
             ### 递归体
            #### 变换两节点指向
            head.next.next = head #### 其中head.next代表下一个节点，再next表示下一个节点的指向。
            head.next = None

            ### 还是new_head 【一直返回新的头节点】
            return new_head

        new_head = dg(head)
        return new_head