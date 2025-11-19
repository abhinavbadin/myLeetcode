class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numset = set(nums)
        value = original

        while value in numset:
            value = value * 2

        return value 