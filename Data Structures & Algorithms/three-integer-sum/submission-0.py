class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L, R = i+1, len(nums)-1

            if nums[i] > 0:
                break

            while L < R:
                sums = nums[i] + nums[L] + nums[R]

                if sums == 0:
                    res.append([nums[i], nums[L], nums[R]])

                    while L < R and nums[L] == nums[L+1]: L += 1
                    while L < R and nums[R] == nums[R-1]: R -= 1

                    L += 1
                    R -= 1

                elif sums < 0:
                    L += 1
                else:
                    R -= 1

        return res


        