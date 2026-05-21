class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #uses hash map to count occurrences of each value
        freq = [[] for i in range(len(nums) + 1)] #same size as input array

        for num in nums:
            count[num] = 1 + count.get(num, 0) #returns 0 if it doesnt exist

        for num, c in count.items(): #returns every key-value pair in our dictionary
            freq[c].append(num) #this value num occurs exactly c times

        res = []
        for i in range(len(freq) - 1, 0, -1): #goes backwards
            for num in freq[i]:
                res.append(num) #takes that num value and appends it to our result
                if len(res) == k: #edge case
                    return res