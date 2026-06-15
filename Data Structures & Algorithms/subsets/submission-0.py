class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtracking(index,cur,res):
            if index==len(nums):
                res.append(cur.copy())
                return 
            backtracking(index+1,cur,res)
            cur.append(nums[index])
            backtracking(index+1,cur,res)
            cur.pop()
        backtracking(0,[],res)
        return res