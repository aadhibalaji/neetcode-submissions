class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        searchRow = 0
        for i in range(len(matrix)):
            if (target >= matrix[i][0]):
                searchRow = i
        
        print(searchRow)

        left = 0;
        right = len(matrix[searchRow]) - 1
      

        while (left <= right):
            current = math.floor((left + right) / 2)

            if (matrix[searchRow][current] == target):
                return True
            elif (matrix[searchRow][current] > target):
                right = current - 1
            else:
                left = current + 1


        return False
            