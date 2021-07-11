class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[0] == '-': return False
        h, t = 0, len(x)-1
        while h < t:
            if x[h] == x[t]:
                h += 1
                t -= 1
                continue
            else: return False
        return True


if __name__ == '__main__':
    x = 121
    result = Solution().isPalindrome(x)
    assert result == True