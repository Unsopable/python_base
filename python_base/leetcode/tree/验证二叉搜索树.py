class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


##### 创建二叉树
none5 = TreeNode(6)
none4 = TreeNode(3)
none3 = TreeNode(4,none4,none5)
none2 = TreeNode(1)
none1 = TreeNode(5,none2,none3)

### 实现 （中序遍历，要是二叉搜索树，则遍历中地前面的数，肯定要小于 后面的数地）

def isValidBST(root):

    ## 如果 根节点是 空，则返回 True
    if not root:
        return True
    ## 如果 根节点 不是空，则进行递归
    ## 如果 左子树 中有 不符合 规则地，则一直返回False,一直到结束
    if not isValidBST(root.left):
        return False

    ## 如果 当前节点的 数值 小与,等于 前面节点的数值，则，返回 False
    global pre
    if pre is not None and root.val <= pre:
        return False

    ## 如果 左子树 都符合规则, 则 将当前节点的值 赋给 pre

    pre = root.val

    ## 如果 右子树 中有 不符合 规则地，则 也一直返回 False，一直到结束
    if not isValidBST(root.right):
        return False

    ### 左子树和右子数都符合 规则，则 返回 True
    return True

pre = None

judge = isValidBST(none1)
print(judge)



