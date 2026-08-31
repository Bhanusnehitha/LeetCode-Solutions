"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
            if head is None:
                return None

            mp={}
            current=head

            while current:
                mp[current]=Node(current.val)
                current=current.next

            current=head

            while current:
                mp[current].next=mp.get(current.next)
                mp[current].random=mp.get(current.random)

                current=current.next

            return mp[head]
