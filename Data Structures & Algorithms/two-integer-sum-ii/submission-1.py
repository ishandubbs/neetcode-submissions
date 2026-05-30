class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        res = []

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                res.extend([left + 1, right + 1])
                break 
            #obtains the num values instead of the indexes, and breaks after
            
            elif current_sum < target:
                left += 1
            
            else:
                right -= 1
            
        return res