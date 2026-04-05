class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = {}
        for s in s1:
            s1_map[s] = s1_map.get(s, 0) + 1

        window_map = {}

        left = 0

        for right in range(len(s2)):
            window_map[s2[right]] = window_map.get(s2[right], 0) + 1
            
            if right-left+1 > len(s1):
                window_map[s2[left]] -= 1
                if window_map[s2[left]] == 0:
                    del window_map[s2[left]]
                left += 1

            if window_map == s1_map:
                return True

        return False
        