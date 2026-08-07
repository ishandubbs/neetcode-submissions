class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = { i:[] for i in range(numCourses) }
        for courses, prereq in prerequisites:
            preReqMap[courses].append(prereq)

        # visitSet = all courses allong the current DFS path
        visitSet = set()
        def dfs(courses):
            if courses in visitSet:
                return False
            if preReqMap[courses] == []:
                return True

            visitSet.add(courses)
            for prereq in preReqMap[courses]:
                if not dfs(prereq): return False
            visitSet.remove(courses)
            preReqMap[courses] = []
            return True

        for courses in range(numCourses):
            if not dfs(courses): return False
        return True

        # 1 -> 2
        # 3 -> 4