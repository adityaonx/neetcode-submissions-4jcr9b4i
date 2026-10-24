class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(list(s))
        t1=sorted(list(t))
        if s1==t1:
            return True
        return False