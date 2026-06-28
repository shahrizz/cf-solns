# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(
    5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
)

def hasPath(node, target):

    if node is None:
        return False

    target -= node.val

    if target:
        return ???

    return (
        hasPath(???, ???)
        or
        hasPath(???, ???)
    )
