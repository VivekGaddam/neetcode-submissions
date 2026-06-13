from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        need = Counter(s1)
        window = Counter(s2[:n1])
        if need == window:
            return True
        l = 0
        for r in range(n1, n2):
            window[s2[r]] += 1
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            if window == need:
                return True

        return False