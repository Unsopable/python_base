
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ### 方法一： 使用 set 集合方法，判断节点是否重复 (52ms,18.7mb)
        ## 创建 set 集合，存放 链表节点
        node_set = set()
        while (head != None):
            ## 未添加节点前，集合的长度
            before_len = len(node_set)
            ## 将当前节点 添加到 集合中
            node_set.add(head)
            ## 添加 节点 后，集合的长度
            after_len = len(node_set)

            ## 如果 添加节点 后，集合长度未变，则有 环
            if (before_len == after_len):
                return True

            ## 下一个节点
            head = head.next
        return False

