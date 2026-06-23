class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #stores pairs of (temperature, index)
        for index, temperature in enumerate(temperatures): #iterates through pairs
            while stack and temperature > stack[-1][0]: #while stack isnt empty and current temperature is warmer than the top of the stack
                previous_temp, previous_index = stack.pop() #colder temperature from the past and the day that occurred
                result[previous_index] = index - previous_index #subtracted colder temperature index from today's index, and saves it into the result
            
            stack.append((temperature, index)) #pushes current day on stack
        
        return result