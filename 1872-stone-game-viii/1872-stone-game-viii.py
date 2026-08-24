class Solution(object):
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Convert stones into prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # Start from the last possible prefix
        dp = stones[-1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            dp = max(dp, stones[i] - dp)

        return dp