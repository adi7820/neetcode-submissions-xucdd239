class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magzine_map = {}

        for ch in magazine:
            magzine_map[ch] = magzine_map.get(ch, 0) + 1

        for ch in ransomNote:
            if magzine_map.get(ch, 0) == 0:
                return False
            magzine_map[ch] -= 1

        return True

        