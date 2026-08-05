class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left = 0
        right = len(nums) - 1

        

        while (left <= right):
            
            current = math.floor((left + right) / 2)
            if (nums[current] == target):
                return current

        
            if (nums[current] > target):
                right = current - 1
            if (nums[current] < target):
                left = current + 1
            

        return -1