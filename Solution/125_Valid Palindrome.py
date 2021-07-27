from collections import deque
import re

class Solution:
    def isPalindrome_deque(self, s: str) -> bool:
        strs = deque()
        for i in s:
            if i.isalnum():
                strs.append(i.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

    def isPalindrom_slice(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    result = Solution().isPalindrome(s)
    assert result == True