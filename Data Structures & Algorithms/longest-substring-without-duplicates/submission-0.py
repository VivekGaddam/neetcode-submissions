class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        visited=set()
        sol=0
        while right<len(s):
            while s[right] in visited:
                visited.remove(s[left])
                left+=1
            visited.add(s[right])
            right+=1
            sol=max(sol,right-left)
        return sol
                