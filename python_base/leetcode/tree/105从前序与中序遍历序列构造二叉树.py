class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:        
            ####### 方法一： 递归
        ### 先写个哈希表（字典），保存中序遍历的每个数值和索引
        inorder_dict = {val:key for key,val in enumerate(inorder)}
        #### 递归方法(参数left 和 right表示列表【每个树】的左右极限索引)
        def dg(pre_left,pre_right,in_left,in_right):
            ## 递归出口
            if pre_left > pre_right:
                return None
            ## 递归体
            ### 创建每个阶段树的头节点
            ## 头节点的值
            rootValue = preorder[pre_left]
            root = TreeNode(rootValue)
            ### 计算该节点左子树一共有多少个值
            leftDistance = inorder_dict[rootValue] - in_left
            ### 递归该节点的左子树头节点
            root.left = dg(pre_left+1,pre_left+leftDistance,in_left,inorder_dict[rootValue]-1)
            ### 递归该节点的右子树头节点
            root.right = dg(pre_left+leftDistance+1,pre_right,inorder_dict[rootValue]+1,in_right)            

            return root


        ## 调用递归函数
        length = len(preorder)
        root = dg(0,length - 1,0,length-1)
        
        return root