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
        output=[]
        for num in nums:
            output.append(product//num)
        return output