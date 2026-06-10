class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        diff=set(nums)
        start=[]
        for i in nums:
            if i-1 not in diff:
                start.append(i)
        if len(nums)==0:
            return 0
        maxi=max(nums)
        sol=0
        for i in start:
            count=0
            for j in range(i,maxi+1):
                if j not in diff:
                    break
                else:
                    count+=1
            sol=max(count,sol)
        return sol
