class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfNum=set()
        for num in nums:
            if num not in setOfNum:
                setOfNum.add(num)
            else:
                return True
        return False