# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Pattern: Arrays & Hashing
# Time: O(n) | Space: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        CD = set()
        for each in nums:
            if each in CD:
                return True
            CD.add(each)
        return False