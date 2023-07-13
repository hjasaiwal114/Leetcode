"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Build adjacency list
        graph = defaultdict(list)
        for pair in prerequisites:
            course, prerequisite = pair
            graph[course].append(prerequisite)

        # Check if there is a cycle
        visited = [0] * numCourses  # 0 - not visited, 1 - visiting, 2 - visited

        def hasCycle(course):
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False

            visited[course] = 1
            for prerequisite in graph[course]:
                if hasCycle(prerequisite):
                    return True

            visited[course] = 2
            return False

        # Perform DFS for each course
        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True