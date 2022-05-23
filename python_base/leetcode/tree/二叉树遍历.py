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

### 实现遍历二叉树(前序遍历)
def validbst(root):

    if root == None:
        return

    print(root.val)
    ## 递归遍历 左边的树叉
    validbst(root.left)
    ## 递归遍历 右边的树叉
    validbst(root.right)

### 运用
validbst(none1)




