from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stone_count = Counter(S)
        result = 0
        for jewel in J:
            if jewel in stone_count.keys():
                result += stone_count[jewel]
        return result


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    result = Solution().numJewelsInStones(jewels, stones)
    assert result == 3