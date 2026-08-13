class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices.copy()

            for source, destination, price in flights:
                if prices[source] == float("inf"):
                    continue
                if prices[source] + price < tempPrices[destination]:
                    tempPrices[destination] = prices[source] + price

            prices = tempPrices

        return -1 if prices[dst] == float("inf") else prices[dst]