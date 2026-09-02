"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head):

        if head is None:
            return head

        def dfs(node):

            current = node
            last = node

            while current:

                next_node = current.next

                if current.child:

                    child_head = current.child

                    child_tail = dfs(child_head)

                    current.next = child_head
                    child_head.prev = current

                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail

                    current.child = None

                    last = child_tail

                else:
                    last = current

                current = next_node

            return last

        dfs(head)

        return head