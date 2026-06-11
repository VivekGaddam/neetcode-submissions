class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_left=[0]*len(height)
        max_right=[0]*len(height)
        maxi=0
        for i in range(len(height)):
            maxi=max(maxi,height[i])
            max_left[i]=maxi
        maxi=0
        for i in range(len(height)-1,-1,-1):
            maxi=max(maxi,height[i])
            max_right[i]=maxi
        ans=0
        for i in range(len(height)):
            ans+=max(0,min(max_left[i],max_right[i])-height[i])
        return ans