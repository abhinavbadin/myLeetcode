class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #1. Build a graph - Adjacency List -> {Node: [(target,weight),...]}
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        #Now eveything is about dijkstra and finding max in the distance table
        
        #2. Build a distance table and initialize prority queue
        dist = {node:float('inf') for node in range(1,n+1)}
        dist[k] = 0
        pq = [(0,k)]

        while pq:
            currdist,node = heapq.heappop(pq)

            if currdist > dist[node]: #outdated entries must be skipped
                continue
            
            for nei,weight in graph[node]:
                newdist = currdist + weight
                
                if newdist < dist[nei]: #if its less than current then update heap
                    dist[nei] = newdist
                    heapq.heappush(pq,(newdist,nei))
        
        #4. get max in dist.values
        mintime = max(dist.values())

        return mintime if mintime!= float('inf') else -1

