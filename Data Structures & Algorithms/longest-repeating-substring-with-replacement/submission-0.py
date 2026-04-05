class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        max_len = 0
        left = 0
        hash_map = {}
        for right in range(len(s)):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1
            max_freq = max(max_freq, hash_map[s[right]])

            while (right-left+1)-max_freq > k:
                hash_map[s[left]] -= 1
                left += 1

            max_len = max(max_len, right-left+1)

        return max_len