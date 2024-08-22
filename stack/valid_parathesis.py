#valid parathesis
class Solution:
    def isValid(self, s: str) -> bool:
        #{[()]}->valid,, {([}])_>invalid

        #bracket opened last should be closed the first
        stack=[]#opening braket
        mapp={')':'(','}':'{',']':'['}
        for c in s:
            if c in mapp:

                openn=stack.pop() if stack else '#'
                if mapp[c]!=openn:
                    return False
            else:
                stack.append(c)
        return not stack
        
