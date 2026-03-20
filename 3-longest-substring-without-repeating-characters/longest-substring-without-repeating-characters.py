# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxLen = 0
        
#         for i in range(0,len(s)):
#             h={}
#             for j in range(i,len(s)):
#                 if s[j] in h:
#                     break
#                     if maxLen<len(h):
#                         maxLen = len(h)
#                     h={}
#                 h[s[j]] = 1
#                 maxLen = max(maxLen,len(h))
              
#         return maxLen


        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0
        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            longest = max(longest, right-left+1)
        return longest
                

