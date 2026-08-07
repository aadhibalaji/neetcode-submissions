class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        
        while len(maxHeap) >= 2:
            stoneOne = -heapq.heappop(maxHeap)
            stoneTwo = -heapq.heappop(maxHeap)

            if stoneOne == stoneTwo:
                continue
            
            if stoneOne >= stoneTwo:
                stoneOne -= stoneTwo
                heapq.heappush(maxHeap, -stoneOne)

        if maxHeap:
            return -maxHeap[0]

        return 0