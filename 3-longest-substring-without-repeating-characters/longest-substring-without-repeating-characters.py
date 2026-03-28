class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in subset:
                subset.remove(s[left])
                left+=1
            subset.add(s[right])
            longest = max(longest, len(s[left:right])+1)
        return longest

