from typing import List
class Solution:
    """ https://leetcode.com/problems/minimum-path-sum/
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
    
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[0 for i in range(cols)] for j in range(rows)]
        
        dp[0][0] = grid[0][0]
        
        for i in range(1, rows):
            dp[i][0] = grid[i][0] + dp[i-1][0]
            
        for j in range(1, cols):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        
        
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                
        return dp[rows-1][cols-1]