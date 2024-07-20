from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastGoodIndex = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= lastGoodIndex:
                lastGoodIndex = i

        return lastGoodIndex == 0
