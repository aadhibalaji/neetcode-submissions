class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left = 0
        right = len(nums) - 1

        cutPoint = None

        while left <= right:

            current = (left + right) // 2

            if (nums[current] > nums[right]):
                left = current + 1
            elif(nums[current] < nums[right] and nums[current - 1] < nums[current]):
                right = current - 1
            else:
                cutPoint = current
                break
        print(cutPoint)

        left = 0
        right = cutPoint - 1

        while (left <= right):
            current = (left + right) // 2

            if (nums[current] == target):
                return current
            elif (nums[current] > target):
                right = current - 1
            else:
                left = current + 1    

    
        left = cutPoint
        right = len(nums) - 1

        while (left <= right):
            current = (left + right) // 2

            if (nums[current] == target):
                return current
            elif (nums[current] > target):
                right = current - 1
            else:
                left = current + 1  

        return -1 
