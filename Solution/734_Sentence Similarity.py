from typing import List
from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if sentence1 == sentence2: return True
        if len(sentence1) != len(sentence2): return False

        similar_dict = defaultdict(list)
        pair_list = []
        for i in similarPairs:
            word1, word2 = i
            similar_dict[word1].append(word2)
            similar_dict[word2].append(word1)

        for sen1, sen2 in zip(sentence1, sentence2):
            pair_list.append([sen1, sen2])

        for i in pair_list:
            word1, word2 = i
            values = similar_dict[word1]
            if word2 in values or word1 == word2:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    # sentence1 = ["great", "acting", "skills"]
    # sentence2 = ["fine", "drama", "talent"]
    # similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
    #
    # sentence1 = ["great"]
    # sentence2 = ["doubleplus", "good"]
    # similarPairs = [["great", "doubleplus"]]
    sentence1 = ["one", "excellent", "meal"]
    sentence2 = ["one", "good", "dinner"]
    similarPairs = [["great", "good"], ["extraordinary", "good"], ["well", "good"], ["wonderful", "good"], ["excellent", "good"],
     ["fine", "good"], ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"], ["the", "one"],
     ["an", "one"], ["single", "one"], ["a", "one"], ["truck", "car"], ["wagon", "car"], ["automobile", "car"],
     ["auto", "car"], ["vehicle", "car"], ["entertain", "have"], ["drink", "have"], ["eat", "have"], ["take", "have"],
     ["fruits", "meal"], ["brunch", "meal"], ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"],
     ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"], ["have", "own"], ["extremely", "very"],
     ["actually", "very"], ["really", "very"], ["super", "very"]]
    result = Solution().areSentencesSimilar(sentence1, sentence2, similarPairs)
    assert result == True