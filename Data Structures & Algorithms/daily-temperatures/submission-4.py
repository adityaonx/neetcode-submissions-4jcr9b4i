class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        for i in range(len(temperatures)):
            day=1
            flag=False
            for j in range(i+1,len(temperatures)):
                if temperatures[i]>=temperatures[j]:
                    day+=1
                else:
                    flag=True
                    break
            if flag:
                result.append(day)
            else:
                result.append(0)
        return result