class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        max_len=0
        seen=set()
        while j<len(s):
            while j<len(s) and s[j] not in seen:
                seen.add(s[j])
                j+=1
            max_len=max(max_len,j-i)
            if j<len(s):
                while s[j] in seen:
                    seen.remove(s[i])
                    i+=1
                seen.add(s[j])
                j += 1
        return max_len