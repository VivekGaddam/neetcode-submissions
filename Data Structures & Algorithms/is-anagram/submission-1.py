from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=Counter(s)
        b=Counter(t)
        if len(a)!=len(b):
            return False
        for i in a:
            if a[i]!=b.get(i,0):
                return False
        return True
