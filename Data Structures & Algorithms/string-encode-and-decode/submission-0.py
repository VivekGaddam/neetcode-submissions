class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            n=len(i)
            s+=f"{n}#{i}"
        return s

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res