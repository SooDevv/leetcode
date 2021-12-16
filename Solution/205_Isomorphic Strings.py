class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}

        for c1, c2 in zip(s, t):
            if (c1 not in s2t) and (c2 not in t2s):
                s2t[c1] = c2
                t2s[c2] = c1
            elif s2t.get(c1) != c2 or t2s.get(c2) != c1:
                return False
        return True