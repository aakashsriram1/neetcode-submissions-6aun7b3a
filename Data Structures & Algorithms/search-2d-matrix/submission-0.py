class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        top = 0 
        bot = row - 1 
        while top <= bot: 
            middle = (top + bot) // 2
            if target > matrix[middle][-1]:
                top = middle + 1 
            elif target < matrix[middle][0]:
                bot = middle - 1 
            else:
                break 
        if not (top <= bot):
            return False
        r = (top + bot) // 2
        left, right = 0, col - 1 
        while left <= right:
            m = ((left+right)// 2)
            if target > matrix[r][m]:
                left = m + 1 
            elif target < matrix[r][m]:
                right = m - 1 
            else:
                return True
        return False