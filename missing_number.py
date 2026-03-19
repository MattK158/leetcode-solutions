class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = len(nums)
        expected = i * (i + 1) // 2
        actual = sum(nums)
        missing = expected - actual
        return missing