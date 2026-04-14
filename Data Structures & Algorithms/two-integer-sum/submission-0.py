class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic1={}
        for i,num in enumerate(nums):
            rem=target-num
            if rem in dic1:
                return [dic1[rem],i]
            dic1[num]=i
        