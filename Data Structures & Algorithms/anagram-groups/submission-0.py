from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            arr=[0]*26
            for j in i:
                arr[ord(j)-ord("a")]+=1
            d[tuple(arr)].append(i)
        ans=[]
        for i in d:
            ans.append(d[i])
        return ans