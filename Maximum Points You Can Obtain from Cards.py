class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        result = 0
        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        for i in range(1,k+1):
            cur_sum = cur_sum - nums[k-i] + nums[-i]
            max_sum = max(cur_sum,max_sum)
        return max_sum