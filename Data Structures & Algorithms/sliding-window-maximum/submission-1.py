class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret=[]
        for i in range(len(nums)-k+1):
            max_len=-float("inf")
            for j in range(k):
                max_len=max(max_len,nums[i+j])
            ret.append(max_len)
        return ret

