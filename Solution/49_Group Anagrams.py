from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for i in strs:
            word = ''.join(sorted(i))
            anagram[word].append(i)
        return anagram.values()


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print(result)
    assert result == [["bat"],["nat","tan"],["ate","eat","tea"]]