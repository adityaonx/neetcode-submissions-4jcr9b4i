class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt_zero=0
        zeros=[0]*len(nums)
        for num in nums:
            if num==0:
                cnt_zero+=1
        if cnt_zero>1:
            return zeros
        product=1
        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i]
        if cnt_zero==1:
            zeros[nums.index(0)]=product
            return zeros
        pref_arr=[1]*len(nums)
        for i in range(1,len(nums)):
            pref_arr[i]=nums[i-1]*pref_arr[i-1]
        suff_arr=[1]*len(nums)
        for j in range(len(nums)-2,-1,-1):
            suff_arr[j]=nums[j+1]*suff_arr[j+1]
        output=[pref_arr[i]*suff_arr[i] for i in range(len(nums))]
        return output

