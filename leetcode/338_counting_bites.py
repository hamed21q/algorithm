import math


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        p = []
        p.append(0)

        for i in range(2, n + 1):
            p.append(p[int(i - math.pow(2, math.floor(math.log(i, 2))))] + 1)

        return p


print(Solution().countBits(0))