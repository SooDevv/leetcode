from typing import List


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        result = []
        while words:
            word = words.pop(0)
            n = len(word)
            indices = [idx for idx, str in enumerate(text) if str == word[0]]
            for idx in indices:
                if text[idx:idx+n] == word:
                    result.append([idx, idx+n-1])
                else:
                    continue
        result.sort()
        return result


if __name__ == '__main__':
    text = "thestoryofleetcodeandme"
    words = ["story", "fleet", "leetcode"]
    result = Solution().indexPairs(text, words)
    assert result == [[3,7],[9,13],[10,17]]