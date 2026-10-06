class Solution:
    def isValid(self, s: str) -> bool:
        r = []
        closeToOpen = {")" : "(", "}" :"{", "]":"["}

        for c in s:
            if c in closeToOpen and r:
                if r[-1] != closeToOpen[c]:
                    return False 
                else:
                    r.pop()

            else:
                r.append(c)
        

        if r: 
            return False
        else:
            return True
                
