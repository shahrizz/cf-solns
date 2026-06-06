from collections import deque

root = [3, 9, 20, None, None, 15, 7]
if root is None:
    return None

queue = deque()
queue.append(root)
ans = []

while queue:
    level = []
    n = len(queue)
    for i in range(n):
        node = queue.popleft()
        level.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        ans.append(level)

return ans
