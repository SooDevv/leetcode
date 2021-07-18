class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            index = haystack.index(needle)
        except ValueError:
            return -1
        return index


if __name__ == '__main__':
    haystack = "aaaaa"
    needle = "bba"
    result = Solution().strStr(haystack, needle)
    assert result == -1