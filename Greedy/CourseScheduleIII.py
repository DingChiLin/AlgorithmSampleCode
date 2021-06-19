from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key = lambda x:x[1])
        queue = []
        time = 0
        for [duration, deadline] in courses:
            time += duration
            heapq.heappush(queue, -duration)
            if time > deadline:
                time -= (-heapq.heappop(queue))

        return len(queue)