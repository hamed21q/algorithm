def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * (n + 1)] * (m + 1)

    for i in reversed(range(m)):
        for j in reversed(range(n)):
            value = float('inf')
            if i < m - 1:
                value = min(value, dp[i + 1][j] + grid[i + 1][j])
            if j < n - 1:
                value = min(value, dp[i][j + 1] + grid[i][j + 1])
            dp[i][j] = min() if value < float('inf') else 0

    return dp[0][0] + grid[0][0]


x = minPathSum([[1, 2, 3], [4, 5, 6]])
print(x)
