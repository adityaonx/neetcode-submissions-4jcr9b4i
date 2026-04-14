from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic1=defaultdict(list)
        for word in strs:
            zeros=[0 for i in range(26)]
            for char in word:
                zeros[ord('a')-ord(char)]+=1
            dic1[tuple(zeros)].append(word)
        return list(dic1.values())