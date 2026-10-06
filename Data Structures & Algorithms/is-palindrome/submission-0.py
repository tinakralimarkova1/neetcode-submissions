class Solution:
    def isPalindrome(self, s: str) -> bool:
        new =''

        for each in s:
            if each.isalnum():
                new += each.lower()
        
        for i in range(len(new)//2):
            if new[i] != new[-1 -i]:
                return False 

        return True