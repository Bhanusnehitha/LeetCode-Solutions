# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, path, total):
            if not node:
                return

            path.append(node.val)
            total += node.val

            # If it is a leaf and sum == targetSum
            if not node.left and not node.right and total == targetSum:
                result.append(path.copy())

            dfs(node.left, path, total)
            dfs(node.right, path, total)

            path.pop()

        dfs(root, [], 0)

        return result