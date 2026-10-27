class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        res=[]
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            sz=int(s[i:j])
            j+=1
            res.append(s[j:j+sz])
            i=j+sz
        return res
        