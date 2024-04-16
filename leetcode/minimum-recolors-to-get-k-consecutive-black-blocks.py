class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        start = 0
        white_count = blocks[:k].count("W")
        ans = white_count
        for end in range(k, n):
            if blocks[start] == "W":
                white_count -= 1
            if blocks[end] == "W":
                white_count += 1
            start += 1
            ans = min(ans, white_count)
        return ans
