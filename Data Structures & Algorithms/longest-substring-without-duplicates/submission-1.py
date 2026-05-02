class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        lo = 0
        result = 0

        for hi in range(len(s)):

            while s[hi] in char_set:
                char_set.remove(s[lo])
                lo += 1

            char_set.add(s[hi])

            result = max(result, (hi - lo + 1))

        return result
        