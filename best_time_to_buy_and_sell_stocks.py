from typing import List
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        low,res = nums[0],0
        for num in nums[1:]:
            if num <low:
                low = num
            elif (num - low) > res:
                res = num - low
        return res
    