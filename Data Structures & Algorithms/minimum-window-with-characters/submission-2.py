from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        d = Counter(t)
        r = len(t) - 1

        if r >= len(s):
            return ""

        sol = ""
        curr = Counter(s[l:r+1])

        while r < len(s):
            # shrink left if unnecessary chars exist
            while (
                l <= r and
                (s[l] not in d or curr[s[l]] > d[s[l]])
            ):
                curr[s[l]] -= 1
                if curr[s[l]] == 0:
                    del curr[s[l]]
                l += 1

            # check validity (>=, not ==)
            for ch in d:
                if curr.get(ch, 0) < d[ch]:
                    break
            else:
                if sol == "" or (r - l + 1) < len(sol):
                    sol = s[l:r+1]

            r += 1
            if r < len(s):
                curr[s[r]] = curr.get(s[r], 0) + 1

        return sol