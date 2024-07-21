from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for m in range(i+1,len(nums)):
                if m>i+1 and nums[m] == nums[m-1]:
                    continue
                j = m + 1
                k = len(nums) - 1

                while j<k:
                    total = nums[i] + nums[j] + nums[k] + nums[m]
                    if total<target:
                        j+=1
                    elif total > target:
                        k -= 1
                    else:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k], nums[m]])))
                        j += 1

                        while nums[j] == nums[j-1] and j<k:
                            j += 1
        return res