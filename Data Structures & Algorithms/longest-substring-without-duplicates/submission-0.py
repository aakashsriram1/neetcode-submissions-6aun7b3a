class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        p1 = p2 = 0 
        seen = set()
        while p2 < len(s): 
            if s[p2] not in seen: 
                longest = max(longest, p2 - p1+1)
                seen.add(s[p2])
                p2 = p2 + 1
            else:
                seen.remove(s[p1])
                p1 = p1 + 1
        return longest