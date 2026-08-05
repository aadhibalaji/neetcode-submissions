class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1


        while left <= right:

            current = (left + right) // 2

            if (nums[current] > nums[right]):
                left = current + 1
            elif(nums[current] < nums[right] and nums[current - 1] < nums[current]):
                right = current - 1
            else:
                return nums[current]    

