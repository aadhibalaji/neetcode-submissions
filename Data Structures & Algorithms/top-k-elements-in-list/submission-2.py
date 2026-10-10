class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        table = {}

        for num in nums:
            table[num] = table.get(num, 0) + 1

        sortedArr = []
        
        for num, cnt in table.items():
            sortedArr.append([cnt, num])

        sortedArr.sort()
        res = []
        while len(res) < k:
            res.append(sortedArr.pop()[1])

        return res
            
        