class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):

            temp = dist[:]

            for u, v, price in flights:

                if dist[u] != INF:
                    temp[v] = min(temp[v], dist[u] + price)

            dist = temp

        if dist[dst] == INF:
            return -1

        return dist[dst]