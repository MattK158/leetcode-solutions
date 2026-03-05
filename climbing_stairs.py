class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        n1 = 1
        n2 = 2
        i = 3
        while i <= n:
            temp = n1 + n2
            n1 = n2
            n2 = temp
            i += 1
        return n2