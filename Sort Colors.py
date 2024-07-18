class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        first,last,i = 0,n-1,0
        while i<last+1:
            if nums[i] == 2:
                nums[i],nums[last] = nums[last],nums[i]
                last -= 1
            elif nums[i] == 0:
                nums[first],nums[i] = nums[i],nums[first]
                first+=1
                i+=1
            else:
                i+=1