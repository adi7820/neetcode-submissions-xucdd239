class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo, hi = 0, len(heights)-1

        res = 0

        while lo < hi:
            h = min(heights[lo], heights[hi])
            w = hi - lo

            res = max(res, (h*w))

            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1

        return res
        