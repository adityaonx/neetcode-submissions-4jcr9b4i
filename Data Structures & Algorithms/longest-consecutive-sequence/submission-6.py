class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check=set(nums)
        max_cnt=0
        cnt=1
        for num in check:
            if num-1 not in check:
                curr_num=num
                cnt=1
                while curr_num+1 in check:
                    cnt+=1
                    curr_num+=1
            max_cnt=max(max_cnt,cnt)
        return max_cnt