class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def back(cur,index,res):
            if sum(cur)>target:
                return 
            elif sum(cur)==target:
                res.append(cur.copy())
                return 
                
            for i in range(index,len(nums)):
                cur.append(nums[i])
                back(cur,i,res)
                cur.pop()
        res=[]
        back([],0,res)
        return res