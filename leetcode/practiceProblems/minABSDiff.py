# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))

# stack = []
# curr = root
# while curr or stack:
#     while curr:
#         stack.append(curr)
#         curr = curr.left
#     curr = stack.pop()
#     print(curr.val)
#     curr = curr.right

# print(stack)
# minDiff = float("inf")


# def findDiff(node: TreeNode):
#     global minDiff
#     if node is None:
#         return
#     if node.left:
#         minDiff = min(minDiff, (node.val - node.left.val))
#     if node.right:
#         minDiff = min(minDiff, (node.right.val - node.val))
#     findDiff(node.left)
#     findDiff(node.right)


# findDiff(root)
# print(minDiff)
minDiff = float("inf")
prev = None


def inorder(node):
    global minDiff, prev

    if node is None:
        return

    inorder(node.left)

    if prev is not None:
        minDiff = min(minDiff, node.val - prev)

    prev = node.val

    inorder(node.right)


inorder(root)
print(minDiff)
