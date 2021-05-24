from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        odd_num = sum([1 for k, v in counter.items() if v % 2 != 0])
        return odd_num <= 1


if __name__ == '__main__':
    s = "code"
    result = Solution().canPermutePalindrome(s)
    assert result == False