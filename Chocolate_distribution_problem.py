from typing import List
class Solution:
    def MinDifference(self, nums: List[int], children: int) -> int:
        res, min=  0, float('inf')
        nums.sort()

        for i in range(len(nums)-children+1):
            j = i + children - 1
