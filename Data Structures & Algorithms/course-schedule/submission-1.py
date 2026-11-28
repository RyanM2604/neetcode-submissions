class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return False

            if adjList[node] == []:
                return True

            visited.add(node)

            for prereq in adjList[node]:
                if not dfs(prereq):
                    return False
            
            visited.remove(node)
            adjList[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True