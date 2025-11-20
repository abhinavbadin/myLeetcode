class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        #Sort the intervals by end time ascending, start descending
        intervals.sort(key=lambda x:(x[1],-x[0]))

        #now chose 2 points posibly include the end point coz that might overlap with future intervals
        chosen = []
        
        for start, end in intervals:
            # Step 1: Count how many chosen numbers fall inside [start, end]
            inside = 0
            for x in reversed(chosen):
                if x>=start:
                    inside+=1
                if inside == 2:
                    break
            
            # Step 2: Add missing numbers (from right end backward)
            while inside < 2:
                new_number = end - (1 - inside)  # adds end, then end-1
                chosen.append(new_number)
                inside += 1

        return len(chosen)