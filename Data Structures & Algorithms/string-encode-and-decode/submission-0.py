class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        op = []
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            temp_str = s[j+1:j+length+1]

            op.append(temp_str)

            i = j + 1 + length

        return op
