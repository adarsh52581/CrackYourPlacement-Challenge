class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first,n = 0,len(nums)
        for i in range(n):
            if nums[i] != 0 :
                nums[first],nums[i] = nums[i],nums[first]
                first += 1