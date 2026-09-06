class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        state = [0] * n

        def dfs(node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            if state[node] == 3:
                return False

            state[node] = 3

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2
            return True

        result = []

        for i in range(n):
            if dfs(i):
                result.append(i)

        return result