class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls2=[i.lower() for i in s if i.isalnum()==True]
        out=ls2
        for i in range(len(out)//2):
            if out[i]!=out[len(out)-1-i]:
                return False
        return True