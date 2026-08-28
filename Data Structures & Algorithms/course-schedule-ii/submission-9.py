from collections import deque
from typing import List


class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> List[int]:

        # courses[b] contains all courses unlocked by completing b
        courses = [[] for _ in range(numCourses)]

        # indeg[a] = number of prerequisites required for course a
        indeg = [0] * numCourses

        for a, b in prerequisites:
            courses[b].append(a)
            indeg[a] += 1

        # Start with courses that have no prerequisites
        q = deque()

        for course in range(numCourses):
            if indeg[course] == 0:
                q.append(course)

        output = []

        # Kahn's algorithm: topological sorting
        while q:
            course = q.popleft()
            output.append(course)

            for next_course in courses[course]:
                indeg[next_course] -= 1

                if indeg[next_course] == 0:
                    q.append(next_course)

        # If not every course was processed, a cycle exists
        if len(output) != numCourses:
            return []

        return output