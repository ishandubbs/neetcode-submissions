class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) 
                # It takes ceil(x / k) time to finish the x pile when Koko 
                # eats at a rate of k bananas per hour.

            if hours <= h:
                result = min(result, k)
                right = k - 1 #need to find a smaller rate
            
            else:
                left = k + 1 #need to find a bigger rate

        return result

