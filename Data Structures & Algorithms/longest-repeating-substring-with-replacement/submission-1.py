class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        result = 0
        lo = 0
        max_freq = 0

        for hi in range(len(s)):
            freq[s[hi]] = freq.get(s[hi], 0) + 1

            max_freq = max(max_freq, freq[s[hi]])

            replacement = (hi - lo + 1) - max_freq

            if replacement > k:
                freq[s[lo]] -= 1
                lo += 1

            result = max(result, (hi - lo + 1))

        return result

        