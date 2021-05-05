class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyborad_dict = {w: i for i, w in enumerate(keyboard)}
        res = 0
        temp = 0
        for c in word:
            res += abs(keyborad_dict[c] - temp)
            temp = keyborad_dict[c]
        return res


if __name__ == '__main__':
    keyboard = "pqrstuvwxyzabcdefghijklmno"
    word = "leetcode"
    result = Solution().calculateTime(keyboard, word)
    assert result == 73
