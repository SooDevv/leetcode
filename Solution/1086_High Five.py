from typing import List
from collections import defaultdict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        score_dict = defaultdict(list)
        result = []

        for item in items:
            id, score = item
            score_dict[id].append(score)
        for id, score in score_dict.items():
            score.sort(reverse=True)
            avg = int(sum(score[:5]) / 5)
            result.append([id, avg])
        return sorted(result)


if __name__ == '__main__':
    items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
    result = Solution().highFive(items)
    assert result == [[1,87],[2,88]]