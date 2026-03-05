class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 1
        maxLen = 0
        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLen = max(maxLen, r - l +1)

        return maxLen