class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ls=set()
        for i in range(len(nums)):
            hashh=set()
            for j in range(i+1,len(nums)):
                k= -(nums[i]+nums[j])
                if k in hashh:
                    ls.add(tuple(sorted([nums[i],nums[j],k])))
                hashh.add(nums[j])
        return list(ls)       