from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n, p, z = [],[],[]
        for num in nums:
            if num>0:
                p.append(num)
            elif num == 0:
                z.append(num)
            else:
                n.append(num)

        N, P = set(n), set(p)
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num,0,num))
        
        if len(z) > 2:
            res.add((0,0,0))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if -1*(n[i]+ n[j]) in P:
                    res.add(tuple(sorted([-1*(n[i]+ n[j]),n[i],n[j]])))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                if -1*(p[i]+ p[j]) in N:
                    res.add(tuple(sorted([-1*(p[i]+ p[j]),p[i],p[j]])))
        return res