class Solution:
    def minCostConnectPoints(self, points):

        n = len(points)

        visited = [False] * n
        min_dist = [float('inf')] * n

        min_dist[0] = 0

        total = 0

        for _ in range(n):

            curr = -1

            # Find unvisited point with minimum cost
            for i in range(n):
                if not visited[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i

            visited[curr] = True
            total += min_dist[curr]

            # Update distances of remaining points
            for i in range(n):

                if not visited[i]:

                    x1, y1 = points[curr]
                    x2, y2 = points[i]

                    distance = abs(x1 - x2) + abs(y1 - y2)

                    min_dist[i] = min(min_dist[i], distance)

        return total