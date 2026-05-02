class Solution:
    def removeDuplicates(self, nums: List[int]):

        slow = 0  # Last unique element ka position

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                # Naya unique element mila!
                slow += 1                   # Next write position
                nums[slow] = nums[fast]     # Wahan likh do

        return slow + 1 