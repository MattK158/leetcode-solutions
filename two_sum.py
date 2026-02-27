class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HM = {}
        for i, each in enumerate(nums):
            if target - each in HM:
                return [HM[target - each], i]
            HM[each] = i