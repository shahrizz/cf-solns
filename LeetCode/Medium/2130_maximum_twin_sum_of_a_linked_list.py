# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
i = head
stack = []
while i:
    stack.append(i.val)
    i = i.next
maxSum = 0
counter = 0
i = head
while counter < (len(stack)) / 2:
    endVal = stack.pop()
    startVal = i.val
    maxSum = max(maxSum, (endVal + startVal))
    i = i.next
    counter += 1

print(maxSum)
