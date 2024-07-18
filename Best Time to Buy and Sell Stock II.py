class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first,second = prices[0],0
        result,i,n = 0,1,len(prices)
        while i < n:
            if prices[i] >= first and prices[i] > second:
                second = prices[i]
                if i == n-1:
                    result += second - first
            elif second != 0:
                result += second - first
                first,second = prices[i],0
            else:
                first = prices[i]
            i += 1
        return result