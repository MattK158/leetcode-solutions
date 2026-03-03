class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        temp = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            if heights[l] < heights[r]:
                temp = heights[l] * (r-l)
                l += 1
            elif heights[l] > heights[r]:
                temp = heights[r] * (r-l)
                r -= 1
            else:
                temp = heights[r] * (r-l)
                l += 1
            if temp > result:
                    result = temp

        return result