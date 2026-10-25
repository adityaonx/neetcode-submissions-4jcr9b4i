from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1=defaultdict(int)
        for num in nums:
            d1[num]+=1
        ls=[]
        for k1,v1 in d1.items():
            ls.append([v1,k1])
        sorted_ls=sorted(ls)[::-1]
        out=[]
        for i in range(0,k):
            out.append(sorted_ls[i][1])
        return out