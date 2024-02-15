class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        o = "("
        c = ")"

        def backtrack(curr, op, cp):
            if op == n and cp == n:
                result.append(curr)
                return
            if op < n:
                backtrack(curr + o, op + 1, cp)
            if cp < op:
                backtrack(curr + c, op, cp + 1)

        backtrack("", 0, 0)
        return result


print(Solution().generateParenthesis(5))
