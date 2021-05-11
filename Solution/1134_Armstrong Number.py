class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        result = 0
        for i in str(n):
            result += pow(int(i), k)
        return n == result


if __name__ == '__main__':
    n = 123
    result = Solution().isArmstrong(n)
    assert result == True