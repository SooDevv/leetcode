import string
from collections import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = string.ascii_lowercase
        char = list(Counter(sentence).keys())
        if len(char) < len(alphabet): return False

        char.sort()
        return True if ''.join(char) == alphabet else False


if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    result = Solution().checkIfPangram(sentence)
    assert result == True