class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def firstIndex():
            lo, hi = 0, len(nums)-1
            
            while lo < hi:
                mid = (lo + hi)//2

                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid

            return lo if nums[lo] == target else -1

        def lastIndex():
            lo, hi = 0, len(nums) - 1

            while lo < hi:
                mid = (lo + hi + 1)//2

                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid

            return lo if nums[lo] == target else -1

        return [firstIndex(), lastIndex()]
        