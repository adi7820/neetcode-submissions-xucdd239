class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi)//2

            banans_eating = sum((p+mid-1)//mid for p in piles)

            if banans_eating <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo
        