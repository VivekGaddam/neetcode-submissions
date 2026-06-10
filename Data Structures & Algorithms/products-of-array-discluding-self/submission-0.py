class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros=nums.count(0)
        if zeros>1:
            return [0]*len(nums)
        product=1
        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i]
            else:
                ind=i
        if zeros==1:
            sol=[0]*len(nums)
            sol[ind]=product
            return sol
        sol=[]
        for i in nums:
            sol.append(product//i)
        return sol
            
