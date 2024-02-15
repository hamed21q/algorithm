class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]

        for i in range(1, numRows):
            be = [1]
            for j in range(1, i):
                be.append(ans[i - 1][j - 1] + ans[i - 1][j])
            be.append(1)
            ans.append(be)
        return ans


print(Solution().generate(4))
