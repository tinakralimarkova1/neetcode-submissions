class Solution:
    def countSubstrings(self, s: str) -> int:
        r = 0

        for i in range(len(s)):
            pointL,pointR = i,i
            while pointL >=0 and pointR < len(s) and s[pointL] == s[pointR]:
                r+=1
                
               
                
                pointL -= 1
                pointR += 1

            pointL,pointR = i,i +1
            while pointL >=0 and pointR < len(s) and s[pointL] == s[pointR]:
                r+=1
                
               
                
                pointL -= 1
                pointR += 1

        return r