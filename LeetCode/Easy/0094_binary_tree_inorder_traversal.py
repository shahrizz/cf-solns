import binarytree

root = binarytree.build([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
ans = []


# deal with left node
# deal with current node
# deal with right node
# inorder principal
def traverse(node):
    if node.left is None and node.right is None:
        ans.append(node.val)
    if node.left is not None:
        traverse(node.left)
    ans.append(node.val)
    if node.right is not None:
        traverse(node.right)
