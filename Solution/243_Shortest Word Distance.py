from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_indices = []
        word2_indices = []
        for idx, word in enumerate(wordsDict):
            if word in [word1, word2]:
                if word == word1:
                    word1_indices.append(idx)
                elif word == word2:
                    word2_indices.append(idx)

        distance = len(wordsDict) -1
        for i in word1_indices:
            for j in word2_indices:
                tmp_dist = abs(i - j)
                if tmp_dist < distance:
                    distance = tmp_dist
        return distance

    # https://leetcode.com/problems/shortest-word-distance/discuss/934595/Python-3-greater-99.31-faster.-O(n)-time-complexity
    def shortestDistance_2(self, words: List[str], word1: str, word2: str) -> int:
        shortestDistance = len(words)
        position1, position2 = -1, -1
        for i in range(len(words)):
            if words[i] == word1:
                position1 = i
            elif words[i] == word2:
                position2 = i

            if position1 != -1 and position2 != -1:
                shortestDistance = min(shortestDistance, abs(position1 - position2))

        return shortestDistance


if __name__ == '__main__':
    wordsDict = ["a","c","b","b","a"]
    word1 = "a"
    word2 = "b"
    result = Solution().shortestDistance(wordsDict, word1, word2)
    assert result == 1