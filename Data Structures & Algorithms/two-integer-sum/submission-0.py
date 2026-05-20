class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Dictionary that stores value:index
        number_map = {}

        #Iterates through collection and keeps track of index
        for i, num in enumerate(nums):
            difference = target - num

            #Check if needed number was already seen
            if difference in number_map:
                return [number_map[difference], i]
            
            #Else add current number and index to map
            number_map[num] = i
        
        return None