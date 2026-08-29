class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(start, path, total):

            # Target reached
            if total == target:
                result.append(path[:])
                return

            # Sum became too large
            if total > target:
                return

            for i in range(start, len(candidates)):

                # Choose
                path.append(candidates[i])

                # Explore
                backtrack(i, path, total + candidates[i])

                # Undo
                path.pop()

        backtrack(0, [], 0)

        return result