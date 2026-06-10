from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        h=[]
        for i in d:
            heapq.heappush(h,(-d[i],i))
        ans=[]
        for _ in range(k):
            ans.append(heapq.heappop(h)[1])
        return ans