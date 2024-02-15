class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = [[1] * n] * m

        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i - 1][j] + d[i][j - 1]

        return d[m - 1][n - 1]


print(Solution().uniquePaths(3, 7))
