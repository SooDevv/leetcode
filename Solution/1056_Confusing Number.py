from collections import Counter


class Solution:
    def confusingNumber(self, n: int) -> bool:
        x, y, cmap = n, 0, {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        while n:
            n, m = divmod(n, 10)
            if m not in cmap: return False
            n, y = n, y * 10 + cmap[m]
        return x != y


if __name__ == '__main__':
    n = 11
    result = Solution().confusingNumber(n)
    assert result == False