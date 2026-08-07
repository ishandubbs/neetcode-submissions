class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prereqs
        preReqMap = { i:[] for i in range(numCourses) }
        for courses, prereq in prerequisites:
            preReqMap[courses].append(prereq)

        # a course has 3 possible states:
        # visited -> courses has been added to output
        # visiting -> courses not added to output, but added to cycle
        # unvisited -> courses not added to output or cycle
        output = []
        visit, cycle = set(), set()
        def dfs(courses):
            if courses in cycle:
                return False
            if courses in visit:
                return True

            cycle.add(courses)
            for prereq in preReqMap[courses]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(courses)
            visit.add(courses)
            output.append(courses)
            return True

        for courses in range(numCourses):
            if dfs(courses) == False:
                return []
        return output