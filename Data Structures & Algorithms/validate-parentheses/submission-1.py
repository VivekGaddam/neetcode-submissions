class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"(":")","{":"}","[":"]"}
        for i in s:
            if i in d:
                stack.append(i)
            else:
                
                if stack and d[stack.pop()]==i:
                    continue
                else:
                    return False

        return True if len(stack)==0 else False