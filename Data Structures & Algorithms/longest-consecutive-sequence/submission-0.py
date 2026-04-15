class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        longest=0
        for i in range(len(nums)):
            if nums[i]-1 not in set1:
                length=1
                while (nums[i]+length) in set1:
                    length+=1
                longest=max(length,longest)
        return longest
