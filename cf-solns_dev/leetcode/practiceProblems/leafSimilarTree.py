class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root1, root2 = (
    TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
        TreeNode(1, TreeNode(9), TreeNode(8)),
    ),
    TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(7)),
        TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))),
    ),
)


leaves1 = []
leaves2 = []


def leafLister(node: TreeNode, currList: list):
    if node is None:
        return
    else:
        if node.left is None and node.right is None:
            currList.append(node.val)
        if node.left:
            leafLister(node.left, currList)
        if node.right:
            leafLister(node.right, currList)


leafLister(root1, currList=leaves1)
leafLister(root2, currList=leaves2)
print(leaves1 == leaves2)
