class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def back(cur,index,res):
            if sum(cur)>target:
                return 
            elif sum(cur)==target:
                res.append(cur.copy())
                return 
                
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                cur.append(candidates[i])
                back(cur,i+1,res)
                cur.pop()
        res=[]
        back([],0,res)
        return res