class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
    
        l = 0
        pointer = l
        r = k - 1
        maxHeap = []

        res = []


        while r <= len(nums) - 1:
            pointer = l
            for num in range(r - l + 1):
                heapq.heappush(maxHeap, -nums[pointer])
                pointer += 1
            
            res.append(-maxHeap[0])
            maxHeap.clear()

            r += 1
            l += 1
    
        return res


            