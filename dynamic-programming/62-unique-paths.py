class Solution:
    """https://leetcode.com/problems/unique-paths/

       Similar Questions:
       https://leetcode.com/problems/unique-paths-ii/

    """
    def uniquePaths(self, m:int, n:int) -> int:
        if m == 1 and n == 1:
            return 1

        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(1,m):
            dp[i][0] = 1

        for j in range(1,n):
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]