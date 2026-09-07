from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for next_course in graph[node]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        if len(result) == numCourses:
            return result

        return []