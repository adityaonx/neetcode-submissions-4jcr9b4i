class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1={}
        for i,num in enumerate(nums):
            rem=target-num
            if rem not in d1:
                d1[num]=i
            else:
                return [d1[rem],i]
