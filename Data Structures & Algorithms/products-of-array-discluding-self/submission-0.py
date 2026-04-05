class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        op = [1]*n

        prefix = 1

        for i in range(n):
            op[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(n-1, -1, -1):
            op[i] *= suffix
            suffix *= nums[i]

        return op


        