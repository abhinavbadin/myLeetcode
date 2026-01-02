class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nmap = Counter(nums)
        for k,v in nmap.items():
            if v > 1:
                return k
        