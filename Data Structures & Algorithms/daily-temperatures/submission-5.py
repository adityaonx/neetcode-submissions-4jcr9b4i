class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                pop_i=stack.pop()
                result[pop_i]=i-pop_i
            stack.append(i)
        return result