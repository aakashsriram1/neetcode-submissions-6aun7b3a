class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0 
        bot = rows - 1 
        #find the row first
        while top <= bot: 
            row = (top+bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        #find out where in the col second
        row = (top + bot) // 2
        left = 0 
        right = cols - 1 
        while left <= right:
            mid = (left+right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False

