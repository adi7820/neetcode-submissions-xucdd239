class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        lo = 0
        result = 0
        curr_sum = 0

        for hi in range(len(nums)):
            curr_sum += nums[hi]

            while nums[hi]*(hi - lo + 1) - curr_sum > k:
                curr_sum -= nums[lo]
                lo += 1

            result = max(result, (hi-lo+1))

        return result
        