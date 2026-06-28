class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
ans = []


def leftSum(node: TreeNode):
    nonlocal ans
    if node is None:
        return
    else:
        if node.left is not None:
            if node.left.left is None and node.left.right is None:
                ans.append(node.left.val)
    leftSum(node.left)
    leftSum(node.right)


leftSum(root)
print(ans)
