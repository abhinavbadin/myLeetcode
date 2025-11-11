class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # (cost, current_city, stops)
        pq = [(0, src, 0)]
        
        # To store best (cost) for (node, stops)
        best = dict()
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            # If destination reached
            if node == dst:
                return cost
            
            # If stops exceed limit
            if stops > k:
                continue
            
            # Explore neighbors
            for nei, price in graph[node]:
                new_cost = cost + price
                
                # Optimization: avoid reprocessing worse states
                if (nei, stops) not in best or new_cost < best[(nei, stops)]:
                    best[(nei, stops)] = new_cost
                    heapq.heappush(pq, (new_cost, nei, stops + 1))
        
        return -1