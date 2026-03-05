class Solution:
    def rob(self, nums: List[int]) -> int:
        b1 = 0
        b2 = nums[0]
        curr = 1
        while curr < len(nums):
            temp = max(nums[curr] + b1, b2)
            b1 = b2
            b2 = temp
            curr += 1
        return b2