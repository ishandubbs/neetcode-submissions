class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)] #array of position, speed pairs (list comprehension)
        stack = []
        for p, s in sorted(pair)[::-1]: #Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #if at least 2 cars and the time that the last car reaches destination before the one ahead of it, we pop from top of stack
                stack.pop()
        return len(stack)
