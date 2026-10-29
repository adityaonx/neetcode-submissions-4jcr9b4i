class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check=set(nums)
        sort_num=sorted(check)
        max_cnt=0
        cnt=1
        for num in sort_num:
            if num+1 in check:
                cnt+=1
            else:
                cnt=1
            max_cnt=max(max_cnt,cnt)
        return max_cnt