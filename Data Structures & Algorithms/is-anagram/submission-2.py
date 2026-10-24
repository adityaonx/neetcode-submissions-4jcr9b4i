class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False    
        seen={}
        for c in s:
            seen[c]=seen.get(c,0)+1
        for c in t:
            if c not in seen:
                return False
            seen[c]=seen[c]-1
        for k,v in seen.items():
            if v!=0:
                return False
        return True