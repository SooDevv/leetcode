class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Time Complexity : O(logn) / Space Complexity : O(1)
        # we're halving it on every second step. we treat the 1/2 of the time as a constant though,
        # so in essence, we say that at each step, num is being halved.
        # when something is halved at every step, it has a O(logn) time complexity.
        # and We only use a constant number of integer variables, and so the space complexity is O(1)
        step = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            step += 1
        return step


if __name__ == '__main__':
    num = 14
    result = Solution().numberOfSteps(num)
    assert result == 6