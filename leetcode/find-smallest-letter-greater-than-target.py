from bisect import bisect_right

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        i = bisect_right(letters, target)
        return letters[0] if i >= len(letters) else letters[i]