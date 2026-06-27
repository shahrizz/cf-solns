# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

ans = True


def checkTree(node):
    global ans

    if node is None:
        return

    if node.left and node.right:
        if node.left.val >= node.right.val or node.val >= node.right.val:
            ans = False

    checkTree(node.left)
    checkTree(node.right)


checkTree(root)
print(ans)
