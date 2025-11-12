class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        #1. Build a graph
        for dest,source in prerequisites:
            graph[source].append(dest)
            indegree[dest]+=1 
        
        #2. declare a dequeu and append ones with index 0
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        topo = []
        count=0

        while q:
            course = q.popleft()
            topo.append(course)
            count+=1

            for nei in graph[course]:
                indegree[nei]-=1

                if indegree[nei]==0:
                    q.append(nei)
        
        if count == numCourses:
            return topo
        else:
            return []