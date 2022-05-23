class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode):
        
        ###### 方法一：DFS（深度优先）
        #### 如果根节点为空，则返回[]
        # if not root:
        #     return []
        # res = []
        
        ##### 递归 ######
        # def dg(root,deepth):
        #     ### 出口
        #     if not root:
        #         return
        #     ### 递归
        #     ### 当前深度
        #     deepth += 1
        #     ### 如果 res 长度没有当前深度大，则添加[]
        #     if len(res) < deepth:
        #         res.append([])
        #     ### 将此时节点的数值放到res对应下标的数组中
        #     res[deepth-1].append(root.val)

        #     ## 左/右边
        #     dg(root.left,deepth)
        #     dg(root.right,deepth)


        # #### 方法二：DFS ######
        # def dg(root,deepth):
        #     ### 出口
        #     if not root:
        #         return
        #     ### 递归
        #     ### 当前深度下的值放到res对应的位置中
        #     try:
        #         res[deepth].append(root.val)
        #     except:
        #         res.append([root.val])
        #     ## 左/右边
        #     dg(root.left,deepth+1)
        #     dg(root.right,deepth+1)
        

        # dg(root,deepth=0)
        # return res


        ######方法三： BFS(广度优先)
        if not root:
            return []
    
        res = []
        ### 第一层只有头节点
        ## queue为栈,更新保存每一层的节点
        queue = [root]

        while queue:
            ## 获取当前层有多少个节点,
            size = len(queue)
            tmp = []
            for _ in range(size):
                ## 从queue栈底出栈
                r = queue.pop(0)
                ### 将该层的数放到tmp中
                tmp.append(r.val)

                ### 出栈节点是否有左右节点,【寻找下一层的数据】
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            res.append(tmp)

        return res