from typing import List
class Solution:
    def maxArea(self, nums: List[int]) -> int: 
        first,last = 0, len(nums)-1
        max = 0
        while first < last:
            cur = min(nums[first], nums[last]) * (last - first)
            if cur> max:
                max = cur
            if nums[first] >= nums[last]:
                last -= 1
            else:
                first += 1
        return max